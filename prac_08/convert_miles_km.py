"""
CP1404 Practical 8
GUI program to convert miles to kilometres
Estimate: 10 minutes
Actual: 20 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertDistanceApp(App):
    """ ConvertDistanceApp is a Kivy App for converting miles to kilometres """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "54.71756"
        return self.root

    def handle_calculate(self):
        """ handle calculation, output result to label widget """
        try:
            result = float(self.root.ids.input_number.text) * 1.60934
        except ValueError:
            result = 0.0
        self.message = str(result)

    def handle_increment(self, increment):
        """ handle incremental change of the input number """
        try:
            value = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + float(increment))
        except ValueError:
            self.root.ids.input_number.text = str(0.0 + float(increment))
        self.handle_calculate()


ConvertDistanceApp().run()
