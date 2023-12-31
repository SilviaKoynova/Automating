import requests


def get_weather(city, units='metric', api_key='5f4197e88f48ab5115d878d138fdd40f'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}"
                       f"\n")



print(get_weather(city='Washington'))
