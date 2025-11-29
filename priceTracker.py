import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Accept-Language": "en-IN,en;q=0.9"
        }
        self.response = requests.get(self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, 'lxml')

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title:
            return title.text.strip()        # remove extra spaces
        return "Title Not Found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-offscreen"})
        if price is not None:
            return price.text.strip()
        return "Price Not Found"


device = PriceTracker("https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/")
print(device.product_title())
print(device.product_price())
