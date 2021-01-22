from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Window.size = (360, 600)
Window.clearcolor = (1, 1, 1, 1)


class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True,
                            row_default_height=40)
        #layout = BoxLayout(orientation="vertical", spacing=10, padding=40)
        label = Label(text=" This is a Universal App",
                      font_size="28sp", bold=True, color=(0, 0, 0, 1), italic=True)
        button = Button(text="Print this", font_size="20sp", size_hint=(0.2, 0.2),
                        pos_hint={'center_x': 0.8, "center_y": 0.8},
                        on_press=self.printpress,
                        on_release=self.printrelease,
                        )
        img = AsyncImage(
            source="http://cdn3.sbnation.com/assets/3786371/DOGE-12.jpg")
        message = TextInput(text="Enter you message here")
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(img)
        layout.add_widget(message)

        return layout

    def printpress(self, obj):
        print("Button pressed")

    def printrelease(self, obj):
        print("Button released")


if __name__ == "__main__":
    MainApp().run()
