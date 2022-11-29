import requests
from bs4 import BeautifulSoup
import lxml




def get_link_data(url):

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
        "Accept-Language":"ar",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    price = soup.select_one(selector="#corePriceDisplay_desktop_feature_div").find('span', class_='a-price-whole').getText()
    price =price[:-1].replace(',', '')
    price = float(price)

    return name, price
