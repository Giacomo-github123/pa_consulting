import kivy
from kivy.app import App
from kivy.uix .label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text = "Your Plants:"))
        self.add_widget(Button(text = "Plant 1"))
        self.add_widget(Button(text = "Plant 2"))

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text = "Plant Name"))
        self.inside.add_widget(Label(text = "Temperature"))
        self.temp = Label(text = '')
        self.inside.add_widget(self.temp)

        self.lvf = Button(text = 'Live plant feed', font_size = 40)
        self.inside.add_widget(self.lvf)

        self.add_widget(self.inside)


'''
class MyGrid(GridLayout):
    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 32
        self.inside.add_widget(Label(text = "Plant Name"))
        self.inside.add_widget(Label(text = "Temperature"))
        self.temp = Label(text = '')
        self.inside.add_widget(self.temp)

        self.lvf = Button(text = 'Live plant feed', font_size = 40)
        self.add_widget(self.lvf)

'''

class MyApp(App):
    def build(self):
        return MyGrid()




if __name__ == "__main__":
    MyApp().run()