import json
import requests
import datetime
import random

url = 'http://127.0.0.1:8000/'

with open('export.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

features = data['features'][:2000]

print(len(features))

for feature in features:
    points = feature['geometry']['coordinates']
    # print(points)
    dct = {
        'address': 'yoq',
        'type_of_building': 'yoq',
        'date': random.randrange(1000, 2023),
        'coordinates': points
    }
    r = requests.post(url + 'home/create_home', json=dct)
    print(r.text)
