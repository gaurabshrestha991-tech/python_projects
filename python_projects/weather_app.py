#   Weather API in Python

import requests

api_key = input("Enter city name: ")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\nWeather Information")
    print("---------------------")
    print("City: ", data["name"])
    print("Temperature: ", data["main"]["temp"], ".c")
    print("Feels Like: ", data["main"]["feels_like"], ".c")
    print("Humidity: ", data["main"]["humidity"], "%")
    print("Weather: ", data['weather'][0]["description"])
    print("Wind Speed: ", data["wind"]["speed"], 'm/s')
else:
    print("City not found or API error.")