import requests
import datetime

API_KEY = "da48ceb91b7b443ca9ca09f71fa1893b"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)

current_parameters = {
    'apiKey' : API_KEY,
    "q" : "movie",
    "from": TODAY,
}

url = 'https://newsapi.org/v2/everything'

response = requests.get(
    url,
    params = current_parameters
    )

print(response.json()['articles'])