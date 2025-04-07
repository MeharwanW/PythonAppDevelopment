from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton , MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# first Empty app

# class TrailApp(MDApp):
#     def build(self):
#         return
#
#
# TrailApp().run()


# Creating Labels
# class TrailApp(MDApp):
#     def build(self):
#         label = MDLabel(text = "Hello Everyone" , halign= "center")
#         return label
#
# TrailApp().run()


#creating buttons
#
# class TrailApp(MDApp):
#     def build(self):
#         screen = Screen()
#         buttonFlat = MDFlatButton(text = "button 1" , _default_theme_text_color =  "Error")
#         screen.add_widget(buttonFlat)
#         return screen
#
#
# TrailApp().run()




class MyWidget(BoxLayout):
    def on_button_click(self):
        self.ids.my_label.text = "Button Clicked!"

    def on_text_validate(self, text):
        self.ids.my_label.text = f"You typed: {text}"

    def on_checkbox_active(self, is_active):
        self.ids.my_label.text = f"Checkbox is {'checked' if is_active else 'unchecked'}"

    def on_spinner_select(self, value):
        self.ids.my_label.text = f"Selected: {value}"

    def on_toggle(self, state):
        self.ids.my_label.text = f"Toggle is {state}"

    def on_slider_change(self, value):
        self.ids.my_label.text = f"Slider value: {int(value)}"

class MyApp(MDApp):
    def build(self):
        Builder.load_file("MDApp.kv")
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()
