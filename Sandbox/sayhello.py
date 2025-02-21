from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

import requests

Builder.load_file("sayhello.kv")  # Manually load KV file

def get_weather():
  URL = "https://api.weatherapi.com/v1/current.json?key=39a96f02b1314125884191955250602&q=minsk&aqi=yes"
  # URL = "https://api.weatherapi.com/v1/current.json?key=39a96f02b1314125884191955250602&q=veracruz&aqi=yes"

  response = requests.get(URL)
  if response.status_code == 200:
    data = response.json()
    print(data)
    icon_url = f'https:{data["current"]["condition"]["icon"]}'
    print(icon_url)

    # Download the image
    img_data = requests.get(icon_url).content
    with open("weather_icon.png", "wb") as handler:
      handler.write(img_data)
  else:
    print("Error fetching data:", response.status_code)


class SayHello(App):
  def build(self):
    self.window = GridLayout()
    self.window.cols = 1
    # #add widgets to window
    
    # get_weather()
    
    self.window.add_widget(Image(source="weather_icon.png"))
    
    return self.window
  

if __name__ == "__main__":
    SayHello().run()