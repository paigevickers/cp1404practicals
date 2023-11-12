"""
CP1404 Practical 8
Dynamically create labels based on content of dictionary
Author: Paige Vickers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamically create labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry
            temp_label = Label(text=name)
            # add the label
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
