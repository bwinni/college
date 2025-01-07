import requests


def get_weather(city):
  """Fetches weather data for a given city."""
  api_key = "a9bc7fdf01d8d6414a3a8901d188402a"  # Replace with your actual API key
  base_url = "https://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city
  response = requests.get(complete_url)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    return None


# Example usage
city = input("Enter city name: ")
weather_data = get_weather(city)

if weather_data:
  print("Weather data for", city, ":")
  celsius_temp = round(weather_data["main"]["temp"] - 273.15, 2)
  print("Temperature (Celsius):", celsius_temp, "(\u00B0C)")

  print("Humidity:", weather_data['main']['humidity'], "U")
  print("Pressure:", weather_data['main']['pressure'], (str)("hPa"))
  print("Wind Speed:", weather_data['wind']['speed'], ("kt")) # to convert knots to mp/h, multiply by knots 1.151
  print("Description:", weather_data['weather'][0]['description'])

else:
  print("City not found or API request failed.")
  
  #Tools > Python > Python Environments > search the packages > install the package, easy as fuck
  #For downloading modules in visual studio code: View, Terminal > specify the path to python, as sometimes python is not rec0gnizing the path. Set the path: $env:path="$env:Path;C:\Python27"
  #then do:  pip install *name of the module*, here we had to install pyowm module that was specified in the documentation on the API website.
  #Python location: C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64