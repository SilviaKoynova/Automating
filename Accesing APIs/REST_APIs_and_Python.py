import requests

r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-9-1&to=2023-9-4&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(content['articles'][0]['title'])