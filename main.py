import config
import requests

LAT: float = 39.738449
LON: float = -104.984848


def fetch_weather_data():
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={config.api_key}")
    response.raise_for_status()

    data = response.json()
    print(data)


fetch_weather_data()
