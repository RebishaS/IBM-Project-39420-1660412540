import requests
import datetime

API_KEY = "da48ceb91b7b443ca9ca09f71fa1893b"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)

sports_parameters = {
    'apiKey' : API_KEY,
    "q" : "sports",
    "from": TODAY,
    "category" : "Sports",
    "language" : "en",
}

url = 'https://newsapi.org/v2/top-headlines/sources'

response = requests.get(
    url,
    params = sports_parameters
    )

print(response.json())