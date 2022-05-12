from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.toast import toast
from simple import *


class Example(MDApp):

    def show_toast(self):
        text = hello()
        toast(text)

    def build(self):
        return Builder.load_file("layout.kv")


Example().run()