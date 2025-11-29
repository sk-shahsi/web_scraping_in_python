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


# device = PriceTracker("https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/")
# print(device.product_title())
# print(device.product_price())
samsung=PriceTracker("https://www.amazon.in/Samsung-Galaxy-Smartphone-Silver-Storage/dp/B0D73TQLFZ/ref=pd_sbs_d_sccl_1_6/523-0276972-1314800?pd_rd_w=u5sZc&content-id=amzn1.sym.6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_p=6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_r=VS1APJ9D6AVNN60NMMS9&pd_rd_wg=b4sSF&pd_rd_r=ef6b90f0-545b-4d52-a87d-b61af2bcd406&pd_rd_i=B0D73TQLFZ&th=1")
print(samsung.product_title())
print(samsung.product_price())