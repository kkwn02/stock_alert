import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from util.stock import *

s = requests.Session();
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://www.ericemanuel.com/collections/products'
itemLink = 'https://www.ericemanuel.com' + findItemLink(s, link, 'boucle', 'Pink')

if itemLink and checkItemStock(s, itemLink, 'XL'):
    itemId = getItemId(s, link, 'XL', 'red')

if itemId:
    print(itemId)
    statusCode = addToCart(s, itemLink, itemId, 'XL')
    if statusCode == 200:
        print('Item added successfully')

checkOut(driver, itemLink, 'boucle', itemId)