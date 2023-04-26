import requests


def get_bitcoin_price():
    resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin&vs_currencies=USD').json
    bitcoin_price = resp.get('bitcoin').get('usd')
    return bitcoin_price
