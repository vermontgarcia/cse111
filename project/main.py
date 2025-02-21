import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock
from datetime import datetime
from kivy.utils import get_color_from_hex


class Controller(FloatLayout):
  '''
    Create a controller that receives widgets from the kv lang file.
    Add actions to be called from the kv lang file.
  '''
  label_one = ObjectProperty()
  info = StringProperty()

  # def do_action(self):
  #   self.label_one.text = 'My label after button press'
  #   self.info = 'New info text'
  

  def fetch_weather(self, city = "provo"):
    '''
      Function to fetch Weather information from API
    '''

    data = {
      'city': 'Provo',
      'temperature': '0°C',
      'conditions': 'Sunny',
      'img_source': 'weather_icon.png',
      'highest': 'H:2°',
      'lowest': 'H:-10°',
    }

    if (city == "provo"):
      update_gui_main(self, data)
    
    # self.info = 'New info text'

  


  # fetch_weather(self)

  def on_load(self):
    '''Call fetch_weather when the app starts'''
    self.fetch_weather()

def update_gui_main(self, data):

  self.city.text = data['city']
  self.temperature.text = data['temperature']
  self.conditions.text = data['conditions']
  self.img_source.source = data['img_source']
  self.highest.text = data['highest']
  self.lowest.text = data['lowest']
  



class RepeaterBox(BoxLayout):
  time_text = StringProperty("Default Time")  # Default value time label
  image_source = StringProperty("weather_icon.png") # Default value for image
  temp_text = StringProperty("0°")  # Default value for temp label

class ControllerApp(App):
  def build(self):
    return Controller(info='Aqui info')

  def on_start(self):
    '''This will be called when the app starts'''
    # Call fetch_weather when the app starts
    self.root.on_load()

if __name__ == '__main__':
  ControllerApp().run()