import requests
import datetime
import json

url = "http://127.0.0.1:8000/"

r = requests.post(url+"delete_home/2")

print(r.text)
