import config
import requests

LAT: float = 39.738449
LON: float = -104.984848


def fetch_weather_data():
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={config.api_key}")
    response.raise_for_status()

    data = response.json()['weather']
    print(data[0]['main'])
    return data[0]['main']


def check_weather(data: str):
    if data == 'rain':
        print('raining today!')
    else:
        print('no rain today')


check_weather(fetch_weather_data())
