import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = f"{db_name}.db"
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        # tells SQLite to return query results as dictionary-like row objects instead of plain tuples.

    def execute(self, sql):
        self.conn.execute(sql) 
        
    def commit(self): 
        self.conn.commit()

    def disconnect(self):
        if self.conn: self.conn.close()





    # def create_table(self):
    #     self.connect()
    #     try:
    #         query = """
    #         CREATE TABLE IF NOT EXISTS students (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name TEXT NOT NULL,
    #             grade INTEGER NOT NULL,
    #             email TEXT NOT NULL UNIQUE
    #         )
    #         """
    #         self.conn.execute(query)
    #         self.conn.commit()
    #     finally:
    #         self.disconnect()

    # def create_student(self, student):
    #     self.connect()
    #     try:
    #         query = "INSERT INTO students (name, grade, email) VALUES (?, ?, ?)"
    #         cursor = self.conn.execute(query, (student.name, int(student.grade), student.email))
    #         self.conn.commit()
    #         return cursor.lastrowid
    #     except sqlite3.IntegrityError:
    #         raise ValueError("Email already exists.")
    #     finally:
    #         self.disconnect()

    # def get_all_students(self):
    #     self.connect()
    #     try:
    #         query = "SELECT * FROM students ORDER BY id"
    #         cursor = self.conn.execute(query)
    #         rows = cursor.fetchall()
    #         students = [Student(row['name'], row['grade'], row['email'], row['id']) for row in rows]
    #         return students
    #     finally:
    #         self.disconnect()

    # def update_student(self, student):
    #     self.connect()
    #     try:
    #         query = "UPDATE students SET name = ?, grade = ?, email = ? WHERE id = ?"
    #         self.conn.execute(query, (student.name, int(student.grade), student.email, student.id))
    #         self.conn.commit()
    #     except sqlite3.IntegrityError:
    #          raise ValueError("Email already exists.")
    #     finally:
    #         self.disconnect()

    # def delete_student(self, student_id):
    #     self.connect()
    #     try:
    #         query = "DELETE FROM students WHERE id = ?"
    #         self.conn.execute(query, (student_id,))
    #         self.conn.commit()
    #     finally:
    #         self.disconnect()


# Data Define Language (SQL)
ddl = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""

ddl_delete="""
DROP TABLE IF EXISTS users
"""

# Data Manipulate Language (SQL)
dml = """
INSERT INTO users (id, name) VALUES (?, ?)
"""

dml2 = """
DELETE FROM users WHERE id = 2
"""

# Data Query Langauge (Select)
dql = """
SELECT * FROM users
"""

if __name__ == '__main__':
    conn = sqlite3.connect("temp.db")
    conn.row_factory = sqlite3.Row
    # tells SQLite to return query results as dictionary-like row objects instead of plain tuples.

    conn.execute(ddl_delete)
    conn.execute(ddl)

    conn.execute(dml, (3, 'sehyun'))
    conn.commit()

    
    # conn.execute(dml2)
    # conn.commit()


    rows = conn.execute(dql).fetchall()
    for row in rows:
        print(f"{row['id']}, {row['name']}")
