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

import requests
import os

# Classes
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
  
  def get_weather(self, city = "provo"):
    '''
      Function to fetch Weather information from API
    '''
    data = fetch_weather(city)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(data)
    current_data = get_current_data(data)
    print(current_data)
    hours_data = build_hours_data(data)
    print(hours_data['0hrs'])
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    if (city == "provo"):
      update_gui_main(self, current_data)
    
    # self.info = 'New info text'
  # fetch_weather(self)

  def on_load(self):
    '''Call fetch_weather when the app starts'''
    self.get_weather()
class RepeaterBox(BoxLayout):
  time_text = StringProperty("Default Time")  # Default value time label
  image_source = StringProperty("icons/weather_icon.png") # Default value for image
  temp_text = StringProperty("0°")  # Default value for temp label

class ControllerApp(App):
  def build(self):
    return Controller(info='Aqui info')

  def on_start(self):
    '''This will be called when the app starts'''
    # Call fetch_weather when the app starts
    self.root.on_load()

# Utility Functions
def update_gui_main(self, data):
  self.city.text = data['city']
  self.temperature.text = data['temperature']
  self.conditions.text = data['conditions']
  self.img_source.source = data['img_source']
  self.highest.text = data['highest']
  self.lowest.text = data['lowest']

def update_gui_forecast(self, data):
  print(data)
  # self.city.text = data['city']
  # self.temperature.text = data['temperature']
  # self.conditions.text = data['conditions']
  # self.img_source.source = data['img_source']
  # self.highest.text = data['highest']
  # self.lowest.text = data['lowest']

def update_gui_hours(self, data):
  print(data)
  # self.city.text = data['city']
  # self.temperature.text = data['temperature']
  # self.conditions.text = data['conditions']
  # self.img_source.source = data['img_source']
  # self.highest.text = data['highest']
  # self.lowest.text = data['lowest']

def get_current_data(data):
  city = data['location']['name']
  temperature = f"{data['current']['temp_c']}°C"
  condition = data['current']['condition']['text']

  icon_url = f"https:{data['current']['condition']['icon']}"
  icon_filename = get_image_filename(icon_url)
  dowload_image(icon_url, icon_filename)

  img_source = f'icons/{icon_filename}'

  highest = f"H:{data['forecast']['forecastday'][0]['day']['maxtemp_c']}°"
  lowest = f"L:{data['forecast']['forecastday'][0]['day']['mintemp_c']}°"

  data_dic = {
    'city': city,
    'temperature': temperature,
    'conditions': condition,
    'img_source': img_source,
    'highest': highest,
    'lowest': lowest,
  }
  return data_dic

def build_hours_data(data):
  hours_dic = {}
  hours = data['forecast']['forecastday'][0]['hour']
  for index, hour in enumerate(hours):
    icon_url = f"https:{hour['condition']['icon']}"
    icon_filename = get_image_filename(icon_url)
    temp = hour['temp_c']
    # Download Icon
    dowload_image(icon_url, icon_filename)
    # Adding data to dictionary
    hours_dic[f'{index}hrs'] = [f'icons/{icon_filename}', temp]
  return hours_dic

def fetch_weather(city):
  print(city)
  URL = f"https://api.weatherapi.com/v1/forecast.json?q={city}&days=3&key=39a96f02b1314125884191955250602"
  response = requests.get(URL)
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("Error fetching data:", response.status_code)

def dowload_image(icon_url, icon_filename):
  if not os.path.exists(f'icons/{icon_filename}'):
    img_data = requests.get(icon_url).content
    with open(f'icons/{icon_filename}', "wb") as handler:
      handler.write(img_data)

def get_image_filename(icon_url):
  # Split the URL get the relevant parts and build filename
  parts = icon_url.split("/")
  image_filename = f"{parts[-2]}-{parts[-1]}"
  return image_filename

if __name__ == '__main__':
  ControllerApp().run()