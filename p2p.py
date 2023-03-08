import requests


async def get_p2p_rates():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        "proMerchantAds": False,
        "page": 1,
        "rows": 10,
        "payTypes": [],
        "countries": [],
        "publisherType": None,
        "asset": "BTC",
        "fiat": "USD",
        "tradeType": "BUY",
        "merchantCheck": False,
        "payTypes": ["TinkoffNew"],
    }

    while True:

        response = requests.post(url, headers=headers, json=params).json()
        return(response['data'][0]['adv']['price'])