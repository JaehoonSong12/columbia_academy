from model import Student, Database

class StudentController:
    def __init__(self, view):
        self.view = view
        self.db = Database()
        self.students = []
        self.current_index = -1
        self.load_students()

    def load_students(self):
        self.students = self.db.get_all_students()
        if self.students:
            self.current_index = 0
            self.show_current_student()
        else:
            self.current_index = -1
            self.view.clear_view()

    def show_current_student(self):
        if 0 <= self.current_index < len(self.students):
            student = self.students[self.current_index]
            data = {
                'id': student.id,
                'name': student.name,
                'grade': student.grade,
                'email': student.email
            }
            self.view.update_view(data)
        elif not self.students:
             self.view.clear_view()

    def prev_record(self):
        if self.students and self.current_index > 0:
            self.current_index -= 1
            self.show_current_student()
        else:
            self.view.show_error("Start of records.")

    def next_record(self):
        if self.students and self.current_index < len(self.students) - 1:
            self.current_index += 1
            self.show_current_student()
        else:
            self.view.show_error("End of records.")

    def new_record(self):
        self.current_index = -1
        self.view.clear_view()

    def save_record(self, data):
        # Create Student object to validate
        try:
            student_id = data.get('id')
            if student_id:
                student_id = int(student_id)
            else:
                student_id = None
                
            student = Student(data['name'], data['grade'], data['email'], student_id)
            
            # Validation
            errors = student.validate()
            if errors:
                self.view.show_error("; ".join(errors))
                return

            if student.id:
                # Update
                self.db.update_student(student)
                self.view.show_success("Record updated.")
            else:
                # Create
                new_id = self.db.create_student(student)
                student.id = new_id
                self.view.show_success("Record created.")
            
            # Reload and navigate to the saved record
            self.load_students()
            # Find the student index
            for i, s in enumerate(self.students):
                if s.id == student.id:
                    self.current_index = i
                    break
            self.show_current_student()

        except ValueError as e:
            self.view.show_error(str(e))
        except Exception as e:
            self.view.show_error(f"An unexpected error occurred: {str(e)}")

    def delete_record(self):
        if 0 <= self.current_index < len(self.students):
            student = self.students[self.current_index]
            try:
                self.db.delete_student(student.id)
                self.view.show_success("Record deleted.")
                self.load_students()
                # Adjust index if necessary
                if self.current_index >= len(self.students):
                    self.current_index = len(self.students) - 1
                self.show_current_student()
            except Exception as e:
                 self.view.show_error(f"Delete failed: {str(e)}")
        else:
            self.view.show_error("No record selected to delete.")
