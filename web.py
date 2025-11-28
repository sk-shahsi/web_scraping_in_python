import urllib.request, urllib.parse, urllib.error

import requests

url = 'http://127.0.0.1:8000/hello/'
# print(dir(requests))
user = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=user)
print(response.content)