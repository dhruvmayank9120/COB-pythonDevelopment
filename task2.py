import requests

# Use the provided OpenWeatherMap API key
API_KEY = '8b6139dd47564ec8470864ef9389ec70'

def fetch_weather(city_name):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Convert to Celsius
        humidity = data['main']['humidity']

        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Humidity: {humidity}%")
    except Exception as e:
        print("Error fetching data")

def get_weather(city_name):
    if city_name:
        fetch_weather(city_name)

# Example usage:
city_name = input("Enter the city name: ")
get_weather(city_name)
