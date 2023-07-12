from kivymd.app import MDApp 
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
class MyApp(MDApp):
    def build(self):
        return MDLabel(text='Hello')
app = MyApp()
app.run()