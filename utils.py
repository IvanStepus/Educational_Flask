import requests


def get_bitcoin_price():
    resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin&vs_currencies=USD').json()
    bitcoin_price = resp.get('bitcoin', {}).get('usd')
    return bitcoin_price


def get_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=ua&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["articles"]
    else:
        return []
