from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class ContainerApp(FloatLayout):
    def main_menu(self):
        pass


class Container(FloatLayout):
    def registration(self):
        if self.sv.text == '8':
            #print('hi')
            #self.sv1.text = 'Здарова заебал'
            return ContainerApp()
        else:
            self.sv1.text = "Не то вводишь псина"
            print('err')

    pass


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
