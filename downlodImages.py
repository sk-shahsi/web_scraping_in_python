import requests
from bs4 import BeautifulSoup

user = input("enter the image name: ")
user_agent = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
url = "https://www.google.com/search?q={user}+images&sca_esv=72036be1bbdfeeb3&udm=2&biw=1536&bih=730&sxsrf=AE3TifP3pBCVLVIiKP27uawZnOxKvQtSoQ%3A1764334047988&ei=35kpafGAPJ6M4-EP2f7MuQ0&ved=0ahUKEwix7MfB8JSRAxUexjgGHVk_M9cQ4dUDCBI&oq=moon+images&gs_lp=Egtnd3Mtd2l6LWltZyILbW9vbiBpbWFnZXMyBxAjGCcYyQIyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMggQABiABBixAzIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHkjnElAAWABwAHgAkAEAmAHOAqABzgKqAQMzLTG4AQzIAQCYAgGgAuECmAMAiAYBkgcDMy0xoAeyBrIHAzMtMbgH4QLCBwMzLTHIBw4&sclient=gws-wiz-img"
response = requests.get(url=url,headers =user_agent).content
print(response)
