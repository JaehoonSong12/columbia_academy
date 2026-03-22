from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class StudentView(Screen):
    def __init__(self, **kwargs):
        super(StudentView, self).__init__(**kwargs)
        self.controller = None 

        # Main Layout
        root_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Header
        header = Label(text="Student Management System", font_size=24, size_hint=(1, 0.1))
        root_layout.add_widget(header)

        # Form Layout
        form_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.5))
        
        form_layout.add_widget(Label(text="ID:"))
        self.id_input = TextInput(readonly=True, multiline=False, background_color=(0.9, 0.9, 0.9, 1))
        form_layout.add_widget(self.id_input)

        form_layout.add_widget(Label(text="Name:"))
        self.name_input = TextInput(multiline=False)
        form_layout.add_widget(self.name_input)

        form_layout.add_widget(Label(text="Grade (1-12):"))
        self.grade_input = TextInput(multiline=False, input_filter='int')
        form_layout.add_widget(self.grade_input)

        form_layout.add_widget(Label(text="Email:"))
        self.email_input = TextInput(multiline=False)
        form_layout.add_widget(self.email_input)

        root_layout.add_widget(form_layout)

        # Navigation Buttons
        nav_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.1))
        self.prev_btn = Button(text="<< Previous")
        self.prev_btn.bind(on_press=self.on_prev)
        self.next_btn = Button(text="Next >>")
        self.next_btn.bind(on_press=self.on_next)
        
        nav_layout.add_widget(self.prev_btn)
        nav_layout.add_widget(self.next_btn)
        root_layout.add_widget(nav_layout)

        # Action Buttons
        action_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.1))
        self.new_btn = Button(text="New", background_color=(0, 0.5, 1, 1))
        self.new_btn.bind(on_press=self.on_new)
        
        self.save_btn = Button(text="Save", background_color=(0, 0.8, 0, 1))
        self.save_btn.bind(on_press=self.on_save)
        
        self.delete_btn = Button(text="Delete", background_color=(1, 0, 0, 1))
        self.delete_btn.bind(on_press=self.on_delete)

        action_layout.add_widget(self.new_btn)
        action_layout.add_widget(self.save_btn)
        action_layout.add_widget(self.delete_btn)
        root_layout.add_widget(action_layout)

        # Status Bar
        self.status_label = Label(text="Ready", size_hint=(1, 0.1), color=(1, 1, 0, 1))
        root_layout.add_widget(self.status_label)

        self.add_widget(root_layout)

    def set_controller(self, controller):
        self.controller = controller

    def on_prev(self, instance):
        if self.controller:
            self.controller.prev_record()

    def on_next(self, instance):
        if self.controller:
            self.controller.next_record()

    def on_new(self, instance):
        if self.controller:
            self.controller.new_record()

    def on_save(self, instance):
        if self.controller:
            data = {
                'id': self.id_input.text,
                'name': self.name_input.text,
                'grade': self.grade_input.text,
                'email': self.email_input.text
            }
            self.controller.save_record(data)

    def on_delete(self, instance):
        if self.controller:
            self.controller.delete_record()

    def update_view(self, data):
        self.id_input.text = str(data.get('id', ''))
        self.name_input.text = data.get('name', '')
        self.grade_input.text = str(data.get('grade', ''))
        self.email_input.text = data.get('email', '')
        self.status_label.text = "Record loaded."
        self.status_label.color = (1, 1, 1, 1)

    def clear_view(self):
        self.id_input.text = ""
        self.name_input.text = ""
        self.grade_input.text = ""
        self.email_input.text = ""
        self.status_label.text = "Enter new details."
        self.status_label.color = (0, 1, 1, 1)

    def show_error(self, message):
        self.status_label.text = f"Error: {message}"
        self.status_label.color = (1, 0, 0, 1)

    def show_success(self, message):
        self.status_label.text = message
        self.status_label.color = (0, 1, 0, 1)
