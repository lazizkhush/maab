import requests

city = input('Enter the name of your city: ')
api_key = '9181fec7f545edcb76efb9016190eeb5'

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=2&appid={api_key}')
lat = response.json()[0]['lat']
lon = response.json()[0]['lon']

weather_info = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
weather_info = weather_info.json()
desc = weather_info['weather'][0]['description']
temp = weather_info['main']['temp']-273.15
humidity = weather_info['main']['humidity']
wind_speed = weather_info['wind']['speed'] 
print(f"Description: {desc}")
print(f'Temprature: {temp:.1f}')
print(f"Humidity: {humidity}")
print(f'Wind Speed: {wind_speed}')



