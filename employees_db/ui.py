import v2_1 as db
from kivy.app import App
import kivy
from kivy.uix.button import Button
kivy.require('1.9.0')

class main(App):
    def build(self):
        return Button(text="press")

main().run()





