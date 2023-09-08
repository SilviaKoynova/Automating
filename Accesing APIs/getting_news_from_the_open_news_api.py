import requests

# r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-9-1&to=2023-9-4&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
# content = r.json()
#
# articles = content['articles']
# print(type(articles))
#
# for article in articles:
#     print('TITLE\n', article['title'], '\nDESCRIPTIOM\n', article['description'])

def get_news(topic, from_date, to_date, language='en', api_key='27104802b05d4f269326b76e71a6d05e'):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTIOM\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2023-9-5', to_date='2023-9-6'))