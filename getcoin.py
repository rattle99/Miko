import requests
import json

def human_format(num, round_to=2):
    if type(num) is str:
        num = float(num)
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'B', 'T'][magnitude])

class Coin: 
    def __init__(self):
        api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/burst/')
        coin = json.loads(api_request.content)
        self.rank = coin[0]['rank']
        self.volume = human_format(coin[0]['24h_volume_usd'], 3)
        self.market_cap = human_format(coin[0]['market_cap_usd'], 3)
        self.price_btc = coin[0]['price_btc']
        self.price_usd = coin[0]['price_usd']
        self.change_1h = coin[0]['percent_change_1h']
        self.change_24h = coin[0]['percent_change_24h']
        self.change_7d = coin[0]['percent_change_7d']

        
if __name__ == '__main__':
    c = Coin()
    print(c.rank)
    print(c.volume)
    print(c.market_cap)
    print(c.price_btc)
    print(c.price_usd)
    print(c.change_1h)
    print(c.change_24h)
    print(c.change_7d)