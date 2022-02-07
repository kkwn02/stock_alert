import requests
from bs4 import BeautifulSoup as soup

def checkStock(session, itemName):
    link = 'https://www.ericemanuel.com/collections/products'
    link2 = 'https://kith.com/collections/kith'
    response = session.get(link)
    if response.status_code != 200:
        return None;
    parsed = soup(response.text, "html.parser")
    # t = parsed.find_all('img', alt='EE® BOUCLE SWEATS')

    t = parsed.find_all('a', href=True)
    # t = parsed.find_all('entry')
    product_links = []
    # colors = ['Purple', 'Orange', 'Pink']
    color = 'Purple'
    plink = ''
    for i in t:
        if i['href'].find('products/products/') != -1:
            product_links.append(i['href'])
            content = i.find_all('noscript')
            for j in content:
                # for color in colors:
                #     if j.find('img')['src'].find(color) != -1:
                #         product_links.append(color)
                if j.find('img')['src'].find(color) != -1:
                    plink = i['href']

    # for i in product_links:
    #     print(i)
    print(plink)



