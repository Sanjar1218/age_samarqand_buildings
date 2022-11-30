import requests
import datetime
import json

url = "http://127.0.0.1:8000/"

data = {
    "address": "samarqand",
    "type_of_building": "uy",
    "date": str(datetime.date.today()),
    "center": {"long": 45, "lat": 45},
    "coordinates": [
        {"long": 45, "lat": 45}
    ]
}

r = requests.post(url+"create_home", json=data)

print(r.text)
