import requests
import datetime

# API_KEY = "da48ceb91b7b443ca9ca09f71fa1893b"
# TODAY = datetime.date.today()
# YESTERDAY = TODAY - datetime.timedelta(days=1)

WEATHER_API_KEY = "f3df3e719ca7ed8234afa1e77b637789"
CITY_NAME = "london"

url = "http://api.openweathermap.org/data/2.5/forecast?"
weather_parameters = {
    "appid" : WEATHER_API_KEY,
    "q" : CITY_NAME,
    
}
response = requests.get(
    url,
    weather_parameters,
)

data = response.json()
print(data)