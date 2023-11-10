from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        self.root.ids.output_label.text = ""  # set output label to blank after clearing
        self.root.ids.input_name.text = ""  # set text field to blank after clearing


BoxLayoutDemo().run()
