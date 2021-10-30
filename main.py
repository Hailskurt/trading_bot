import ccxt
import time
import os

binance = ccxt.binance()
ftx = ccxt.ftx()

ticker = os.getenv['TICKER', 'BTC/USD']
min_spread = os.getenv['MIN_SPREAD', 10]
delay = os.getenv['DELAY', 1]

print(f'Ticker: {ticker},   min spread: {min_spread}')
print()

while True:
    time.sleep(delay)
    bid = binance.fetch_ticker(ticker)['bid']
    ask = ftx.fetch_ticker(ticker)['ask']
    if bid - ask >= min_spread:
        print(f'Binance bid: {bid}     FTX ask: {ask}     spread: {round(bid-ask, 5)}     {time.ctime()}')