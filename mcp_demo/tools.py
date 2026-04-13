import requests
import database

API_KEY = "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"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={ed5b482a9cmshd7c43a6e396f0e7p1b4fc7jsne569b39ecb51}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "City not found"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"The weather in {city} is {temp}°C with {desc}"
    except:
        return "Error fetching weather"


def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"


def get_employee(emp_id):
    return database.get_employee(emp_id)