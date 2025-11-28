import requests

url = "http://127.0.0.1:8000/hello/"

response = requests.get(url=url)

print(type(response.text))