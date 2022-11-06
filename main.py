import config
import requests
from twilio.rest import Client

client = Client(config.twilio_SID, config.twilio_auth_token)

LAT: float = 39.738449
LON: float = -104.984848


def fetch_weather_data():
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={config.api_key}")
    response.raise_for_status()

    data = response.json()['weather']
    print(data[0]['main'])
    return data[0]['main']


def check_weather(data: str):
    message = client.messages.create(body=f"{data}", from_=config.twilio_phone_number, to=config.personal_number)

    print(message.sid)


check_weather(fetch_weather_data())
