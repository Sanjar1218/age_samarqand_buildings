import requests

url = 'http://127.0.0.1:8000/'

r = requests.get(url+'get_homes')

print(r.text)
