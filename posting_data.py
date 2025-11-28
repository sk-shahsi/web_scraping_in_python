import requests

url = "http://127.0.0.1:8000/post/"

payload = {
    "title" : "greting",
    "content" : "this is post from web scraping."
}
response = requests.get(url=url,data=payload)

print(response.text)