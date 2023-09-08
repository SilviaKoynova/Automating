import requests

def get_news(country, api_key='27104802b05d4f269326b76e71a6d05e'):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTIOM\n', {article['description']}")
    return results

print(get_news(country='us'))