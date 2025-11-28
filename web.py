import urllib.request, urllib.parse, urllib.error

import requests

url = 'http://127.0.0.1:8000/hello/'
# print(dir(requests))
response = requests.get(url=url)
print(response.request.headers)