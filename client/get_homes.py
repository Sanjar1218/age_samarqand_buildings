import requests

url = 'http://127.0.0.1:8000/home/'

r = requests.get(url+'get_homes')

print(r.text)
