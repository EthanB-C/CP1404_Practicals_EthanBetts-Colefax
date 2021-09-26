from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesToKM(App):
    message = StringProperty()

    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_kilometres(self, input_miles):
        try:
            miles = int(input_miles)
            kilometres = miles * 1.609
            self.message = str(kilometres)
        except ValueError:
            self.message = '0.0'

    def handle_increment(self, increment):
        try:
            new_input_miles = int(self.root.ids.user_input.text) + increment
            self.root.ids.user_input.text = str(new_input_miles)
        except ValueError:
            self.root.ids.user_input.text = str(0 + increment)


ConvertMilesToKM().run()
