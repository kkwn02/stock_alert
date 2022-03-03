import os
import requests
from twilio.rest import Client

def get_json(session, item_id):
    if item_id:
        response = session.get(f'https://www.supremenewyork.com/shop/{item_id}.json')
    else:
        response = session.get('https://www.supremenewyork.com/mobile_stock.json')
    if response.status_code == 200:
        return response.json()
    return None

def get_item_id(stocklist, category, item):
    for i in (stocklist['products_and_categories']):
        print(i)
    for stock in stocklist['products_and_categories'][category]:
        if stock['name'] == item:
            return stock['id']
    return None


def check_item_stock(json, color, size):
    for style in json['styles']:
        if style['name'] == color:
            for sz in style['sizes']:
                if sz['name'] == size and sz['stock_level']:
                    return True
    return False

def perform_tasks(category, itemName, itemColor, itemSize):
    s = requests.Session();
    stocklist = get_json(s, None)
    if stocklist:
        item_id = get_item_id(stocklist, category, itemName)
    if item_id:
        return check_item_stock(get_json(s, item_id), itemColor, itemSize)

def send_msg(itemName, itemColor, itemSize, number):
    account_sid = 'ACf01b5f7ae5978908c2371f02b76282b3'
    auth_token = 'fe3f1cd228c99ef351f0a90e5d90ec73'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Alert: {itemName} in {itemColor}, size {itemSize} is in stock",
        from_='+18594847581',
        to=number
    )
    return message.sid