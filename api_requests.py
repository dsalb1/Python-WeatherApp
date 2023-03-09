import requests
from WeatherData import WeatherData
import json


# build api call to Open Weather Map and returns a response
def build_weather_api_call(city_name):
    apiKey = 'somevalidkey' # get your own damn key
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&units=metric&appid=' + apiKey
    response = requests.get(url)
    response.raise_for_status()
    return response


# parses the Open Weather Map API response with the Python json library and constructs a WeatherData object
def build_weather_data(city_name):
    api_call = build_weather_api_call(city_name)
    data = json.loads(api_call.text)
    description = data.get('weather')[0].get('description').upper()
    temperature = data.get('main').get('temp')
    city_weather = WeatherData(city_name, description)
    city_weather.getTemperature(temperature)
    return city_weather
