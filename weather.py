# weather.py

import requests
from config import API_KEY, BASE_URL


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\nWeather Report")
        print("----------------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", description)
        print("Wind Speed:", wind_speed, "m/s")

    else:
        print("City not found or API error")


city_name = input("Enter city name: ")
get_weather(city_name)