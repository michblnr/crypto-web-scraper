from bs4 import BeautifulSoup
import requests


url = "https://coinmarketcap.com";
result = requests.get(url);
doc = BeautifulSoup(result.text, 'html.parser');

tbody = doc.tbody;
tableRow = tbody.contents;

prices = {};

for tr in tableRow[:10]:
    name, price = tr.contents[2:4]
    fixedName = name.p.string
    fixedPrice = price.span.string
    #print(price)
    #fixedPrice = price.a.string

    prices[fixedName] = fixedPrice;

print(prices);



