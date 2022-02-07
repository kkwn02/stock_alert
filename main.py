import requests
from util.stock import checkStock

s = requests.Session();

response = checkStock(s, 'Bouncle')
if  response != None:
    print(response)
