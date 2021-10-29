import ccxt
import time
import json

binance = ccxt.binance()
ftx = ccxt.ftx()

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

ticker = config['ticker']
min_spread = config['min_spread']

print(f'Ticker: {ticker},   min spread: {min_spread}')
print()

while True:
    time.sleep(1)
    bid = binance.fetch_ticker(ticker)['bid']
    ask = ftx.fetch_ticker(ticker)['ask']
    if bid - ask >= min_spread:
        print(f'Binance bid: {bid}     FTX ask: {ask}     spread: {round(bid-ask, 5)}     {time.ctime()}')