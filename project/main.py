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
# import geocoder

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
  
  def get_weather(self):
    '''
      Function to fetch Weather information from API
    '''
    current_city = get_current_city()

    data = fetch_weather(current_city)

    update_gui_main(self, get_current_data(data))
    update_gui_hours(self, build_hours_data(data))
      
    
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

def get_current_city():
  try:
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    current_city = data.get("city", "Unknown City")
    return current_city
  except:
    return("provo") # If fails it defaults city to Provo UT

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

  keys_list = list(data.keys())  # Convert dictionary keys to a list
  print(keys_list)
  
  self.hrs0.image_source = data['hrs0'][0]
  self.hrs0.temp_text = data['hrs0'][1]
  self.hrs1.image_source = data['hrs1'][0]
  self.hrs1.temp_text = data['hrs1'][1]
  self.hrs2.image_source = data['hrs2'][0]
  self.hrs2.temp_text = data['hrs2'][1]
  self.hrs3.image_source = data['hrs3'][0]
  self.hrs3.temp_text = data['hrs3'][1]
  self.hrs4.image_source = data['hrs4'][0]
  self.hrs4.temp_text = data['hrs4'][1]
  self.hrs5.image_source = data['hrs5'][0]
  self.hrs5.temp_text = data['hrs5'][1]
  self.hrs6.image_source = data['hrs6'][0]
  self.hrs6.temp_text = data['hrs6'][1]
  self.hrs7.image_source = data['hrs7'][0]
  self.hrs7.temp_text = data['hrs7'][1]
  self.hrs8.image_source = data['hrs8'][0]
  self.hrs8.temp_text = data['hrs8'][1]
  self.hrs9.image_source = data['hrs9'][0]
  self.hrs9.temp_text = data['hrs9'][1]
  self.hrs10.image_source = data['hrs10'][0]
  self.hrs10.temp_text = data['hrs10'][1]
  self.hrs11.image_source = data['hrs11'][0]
  self.hrs11.temp_text = data['hrs11'][1]
  self.hrs12.image_source = data['hrs12'][0]
  self.hrs12.temp_text = data['hrs12'][1]
  self.hrs13.image_source = data['hrs13'][0]
  self.hrs13.temp_text = data['hrs13'][1]
  self.hrs14.image_source = data['hrs14'][0]
  self.hrs14.temp_text = data['hrs14'][1]
  self.hrs15.image_source = data['hrs15'][0]
  self.hrs15.temp_text = data['hrs15'][1]
  self.hrs16.image_source = data['hrs16'][0]
  self.hrs16.temp_text = data['hrs16'][1]
  self.hrs17.image_source = data['hrs17'][0]
  self.hrs17.temp_text = data['hrs17'][1]
  self.hrs18.image_source = data['hrs18'][0]
  self.hrs18.temp_text = data['hrs18'][1]
  self.hrs19.image_source = data['hrs19'][0]
  self.hrs19.temp_text = data['hrs19'][1]
  self.hrs20.image_source = data['hrs20'][0]
  self.hrs20.temp_text = data['hrs20'][1]
  self.hrs21.image_source = data['hrs21'][0]
  self.hrs21.temp_text = data['hrs21'][1]
  self.hrs22.image_source = data['hrs22'][0]
  self.hrs22.temp_text = data['hrs22'][1]
  self.hrs23.image_source = data['hrs23'][0]
  self.hrs23.temp_text = data['hrs23'][1]

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
    hours_dic[f'hrs{index}'] = [f'icons/{icon_filename}', f'{temp}']
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