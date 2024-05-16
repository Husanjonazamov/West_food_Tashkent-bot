import requests
from config.settings import BASE_URL

def getBasketList(user_id):
    url = BASE_URL + f"food/busket-list?user_id={user_id}"
    response = requests.get(url)
    return response.json()


def getBasketItem(basket_id):
    response = requests.get(BASE_URL + f"food/busket-item?basket_id={basket_id}")
    return response.json()


def changeBasketItem(basket_id, action):
    response = requests.get(BASE_URL + f'/food/busket-change?basket_id={basket_id}&action={action}')
    return response.json()

def clearBasketItem(user_id):
    response = requests.get(BASE_URL + f'/food/busket-clear?user_id={user_id}')
    return response.json()