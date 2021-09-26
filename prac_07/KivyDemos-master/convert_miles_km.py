from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesToKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_kilometres(self, user_input):
        miles = int(user_input)
        kilometres = miles * 1.609
        self.root.ids.output_text.text = str(kilometres)


ConvertMilesToKM().run()
