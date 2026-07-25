import requests

API_KEY = "YOUR_OPENWEATHER_KEY"


def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=30)

    data = response.json()

    if response.status_code != 200:
        return "Weather information unavailable."

    return (
        f"Temperature: {data['main']['temp']}°C\n"
        f"Weather: {data['weather'][0]['description']}\n"
        f"Humidity: {data['main']['humidity']}%"
    )