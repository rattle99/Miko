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
 
def getCoinData():
    api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/burst/')
    coin = json.loads(api_request.content)
    
    print('Rank: ', coin[0]['rank'], '\n')
    print('Price: ', coin[0]['price_usd'], '\n')
    print('Price: ', coin[0]['price_btc'], '\n')
    print('Volume: ', coin[0]['24h_volume_usd'], '\n')
    print('Market Cap: ', coin[0]['market_cap_usd'], '\n')
    print('Change 1H: ', coin[0]['percent_change_1h'], '\n')
    print('Change 24H: ', coin[0]['percent_change_24h'], '\n')
    print('Change 7D: ', coin[0]['percent_change_7d'], '\n')
    print(human_format(coin[0]['market_cap_usd']))

if __name__ == '__main__':
    getCoinData()