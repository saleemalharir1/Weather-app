import requests 
import json

def get_weather_data(location, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    return json.loads(response.text)

def kelvin_to_fahrenheit(temp):
    return round((temp - 273.15) * 9/5 + 32, 1)

def display_weather_data(weather_data):
    print(f'Current temperature: {kelvin_to_fahrenheit(weather_data["main"]["temp"])}°F')
    print(f'Feels like: {kelvin_to_fahrenheit(weather_data["main"]["feels_like"])}°F')
    print(f'Humidity: {weather_data["main"]["humidity"]}%')
    print(f'Wind speed: {weather_data["wind"]["speed"]} mph')
    print(f'Weather description: {weather_data["weather"][0]["description"]}')
    
api_key = '966bd25bdb896fd432cc0831776a9e8b'
location = input('Enter location: ')
weather_data = get_weather_data(location, api_key)
display_weather_data(weather_data)