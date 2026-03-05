# view.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=20, **kwargs)

        self.label = Label(
            text="Enter text and press the button",
            font_size=20,
            size_hint_y=None,
            height=50,
        )

        self.text_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
        )

        self.button = Button(
            text="Update Label",
            size_hint_y=None,
            height=50,
        )
        self.button.bind(on_press=self.update_label)

        self.add_widget(self.label)
        self.add_widget(self.text_input)
        self.add_widget(self.button)

    def update_label(self, instance):
        self.label.text = self.text_input.text or "Empty input"


class SimpleApp(App):
    def build(self):
        return SimpleLayout()


if __name__ == "__main__":
    SimpleApp().run()
    # python view.py
