import json
import requests
import datetime

url = 'http://127.0.0.1:8000/'

with open('export.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

features = data['features'][:10]

for feature in features:
    points = feature['geometry']['coordinates']
    print(points)
    dct = {
        'address': 'yoq',
        'type_of_building': 'yoq',
        'date': str(datetime.date.today()),
        'coordinates': points
    }
    r = requests.post(url + 'home/create_home', json=dct)
    print(r.text)
