from kivy.app import App
from kivy.uix.button import Button


class Teste(App):
    def build(self):
        return Button(text='Olá Mundo!')


Teste().run()