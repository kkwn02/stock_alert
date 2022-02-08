import requests
from bs4 import BeautifulSoup as soup
import json
import re

def findItemLink(session, productsLink, itemName, color):
    response = session.get(productsLink)
    if response.status_code != 200:
        return None
    parsed = soup(response.text, "html.parser")
    t = parsed.find_all('a', href=True)
    plink = None
    for i in t:
        if i['href'].find('products/products/') != -1 and i['href'].find(itemName) != -1:
            content = i.find_all('noscript')
            for j in content:
                if j.find('img')['src'].find(color) != -1:
                    plink = i['href']
    return plink

def checkItemStock(session, productLink, itemSize):
    response = session.get(productLink)
    if response.status_code != 200:
        return None
    parsed = soup(response.text, "html.parser")
    t = parsed.find_all(attrs={'data-value': itemSize})

    for i in t:
        if len(i.find('input')['class']) > 1:
            return False
    return True

def getItemId(session, productsLink, size, color):
    response = session.get(productsLink)
    if response.status_code != 200:
        return None
    bs = soup(response.text, "html.parser")
    scripts = bs.find_all('script')
    itemId = None
    for script in scripts:
        if script.text.find('var meta') != -1:
            sstr = str(script.string)
            idstr = sstr[sstr.find('var meta'):sstr.find('for (')]
            jsonvar, trash, jsonstr = idstr.partition(' = ')
    jsonlist = re.findall(r'\{"id":[0-9]{14}.+?"}',jsonstr)
    for i in jsonlist:
        jsonObj = json.loads(i)
        if jsonObj['public_title'] == size and jsonObj['sku'].lower().find(color) != -1:
            itemId = (jsonObj['id'])
    return itemId


def addToCart(session, productLink, itemId, size):
    payload = {
        'form_type': 'product',
        # 'utf8': '%E2%9C%93',
        'Size': size,
        'id': itemId
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.ericemanuel.com',
        'Authority': 'www.ericemanuel.com'
    }
    url = 'https://www.ericemanuel.com/cart/add.js'
    response = session.post(url, headers=headers, data=payload)
    return response.status_code



