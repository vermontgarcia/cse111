from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import requests
import os

# Load the .kv file
Builder.load_file('weather.kv')

def get_weather(instance, city = 'veracruz'):
  '''Fetch weather Data from API and update UI'''
  API_KEY = '9cbb5f046e61893ea92077d98bb1de3f'
  URL = f'https://api.weatherapi.com/v1/current.json?key=39a96f02b1314125884191955250602&q={city}&aqi=yes'
  # URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
  
  response = requests.get(URL)
  if response.status_code == 200:
    data = response.json()
    print(data)
    icon_url = f"https:{data['current']['condition']['icon']}"





    # Download and save the image
    img_data = requests.get(icon_url).content
    with open('weather_icon.png', 'wb') as handler:
      handler.write(img_data)
    


    # Trigger UI update (run in main thread)
    # instance.update_image()
  else:
    print('Error fetching data:', response.status_code)

class WeatherApp(GridLayout):
  # Initialize Main Layout
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.cols = 1
    # self.rows = 12
    
    # City Label
    self.city = Label(text="Provo", font_size = 40)
    self.add_widget(self.city)
    
    # City Label
    self.temperature = Label(text="7°C", font_size = 72)
    self.add_widget(self.temperature)
    
    # City Label
    self.condition = Label(text="Cloudy", font_size = 30)
    self.add_widget(self.condition)
    
    # Add Image to layout
    self.image = Image(source='weather_icon.png')
    self.add_widget(self.image)






    # Fetch weather icon on startup with 1 second delay
    Clock.schedule_once(lambda dt: get_weather(self), 1)

  def update_image(self):
    '''Refresh image in the UI'''
    self.image.source = 'weather_icon.png'
    self.image.reload()  # Force image update

class Weather(App):
  def build(self):
    return WeatherApp()

if __name__ == '__main__':
    Weather().run()
