import requests
import json

url = "https://graph.facebook.com/v17.0/no?fields=link%2Cimages&access_token=no"
response = requests.get(url)
data = response.text
data = json.loads(data)
image_url = data['images'][0]['source']
image_bytes = requests.get(image_url).content
with open('image_jpg', 'wb') as file:
    file.write(image_bytes)
