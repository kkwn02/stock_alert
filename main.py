import requests
from util.stock import *

s = requests.Session();

link = 'https://www.ericemanuel.com/collections/products'
itemLink = 'https://www.ericemanuel.com' + findItemLink(s, link, 'boucle', 'Pink')

if itemLink and checkItemStock(s, itemLink, 'XL'):
    itemId = getItemId(s, link, 'XL', 'red')

if itemId:
    print(itemId)
    statusCode = addToCart(s, itemLink, itemId, 'XL')
    if statusCode == 200:
        print('Item added successfully')


