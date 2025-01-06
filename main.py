from kivy.uix.actionbar import BoxLayout
import kivy
from kivy.app import App
from kivy.uix.label import Label
import random

kivy.require('1.9.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(1, 1000))

class RandomInteger(App):

    def build(self):
        return MyRoot()
    

randominteger = RandomInteger()

randominteger.run()