import sqlite3
import re

class Student:
    def __init__(self, name, grade, email, student_id=None):
        self.id = student_id
        self.name = name
        self.grade = grade
        self.email = email

    def validate(self):
        """
        Validates the student data.
        Returns a list of error messages. If empty, data is valid.
        """
        errors = []
        if not self.name or len(self.name.strip()) < 2:
            errors.append("Name must be at least 2 characters long.")
        
        if not self.grade:
             errors.append("Grade is required.")
        else:
            try:
                g = int(self.grade)
                if g < 1 or g > 12:
                    errors.append("Grade must be between 1 and 12.")
            except ValueError:
                errors.append("Grade must be a number.")

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not self.email or not re.match(email_regex, self.email):
            errors.append("Invalid email address.")

        return errors

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', grade={self.grade}, email='{self.email}')"


class Database:
    def __init__(self, db_name="school.db"):
        self.db_name = db_name
        self.conn = None
        self.create_table()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        self.connect()
        try:
            query = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """
            self.conn.execute(query)
            self.conn.commit()
        finally:
            self.disconnect()

    def create_student(self, student):
        self.connect()
        try:
            query = "INSERT INTO students (name, grade, email) VALUES (?, ?, ?)"
            cursor = self.conn.execute(query, (student.name, int(student.grade), student.email))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists.")
        finally:
            self.disconnect()

    def get_all_students(self):
        self.connect()
        try:
            query = "SELECT * FROM students ORDER BY id"
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            students = [Student(row['name'], row['grade'], row['email'], row['id']) for row in rows]
            return students
        finally:
            self.disconnect()

    def update_student(self, student):
        self.connect()
        try:
            query = "UPDATE students SET name = ?, grade = ?, email = ? WHERE id = ?"
            self.conn.execute(query, (student.name, int(student.grade), student.email, student.id))
            self.conn.commit()
        except sqlite3.IntegrityError:
             raise ValueError("Email already exists.")
        finally:
            self.disconnect()

    def delete_student(self, student_id):
        self.connect()
        try:
            query = "DELETE FROM students WHERE id = ?"
            self.conn.execute(query, (student_id,))
            self.conn.commit()
        finally:
            self.disconnect()
