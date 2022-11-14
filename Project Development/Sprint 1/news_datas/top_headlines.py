import requests
import datetime

API_KEY = "da48ceb91b7b443ca9ca09f71fa1893b"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)
COUNTRY = "in"
CATEGORY = "business"

top_headline_parameters = {
    'apiKey' : API_KEY,
    # "q" : "top-headlines",
    "country" : COUNTRY,
    "category" : CATEGORY,
    "from": TODAY,
}

url = 'https://newsapi.org/v2/top-headlines'

response = requests.get(
    url,
    params = top_headline_parameters
    )

articles = response.json()['articles']

title = [article['title'] for article in articles]
description = [article['description'] for article in articles]
url = [article['url'] for article in articles]
author = [article['author'] for article in articles]
url_to_image = [article['urlToImage'] for article in articles]

print(url_to_image)