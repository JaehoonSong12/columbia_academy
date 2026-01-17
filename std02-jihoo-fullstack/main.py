from kivy.app import App
from kivy.core.window import Window
from view import StudentView
from controller import StudentController

class StudentApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Dark background
        self.title = "Student Management System"
        
        # Initialize View
        view = StudentView(name='main_screen')
        
        # Initialize Controller
        controller = StudentController(view)
        
        # Link View to Controller
        view.set_controller(controller)
        
        return view

if __name__ == '__main__':
    StudentApp().run()
