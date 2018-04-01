import httphelper
import requests

def get_referencedata():

    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

def get_compaydata(ticker):
    url = 'https://api.iextrading.com/1.0/stock/{0}/company'.format(ticker)
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

def get_dividenddata(ticker):
    # get months dividend list to make sure won't miss anyone
    url = 'https://api.iextrading.com/1.0/stock/{0}/dividends/6m'.format(ticker)
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

def get_splitdata(ticker):
    # get months dividend list to make sure won't miss anyone
    url = 'https://api.iextrading.com/1.0/stock/{0}/splits/6m'.format(ticker)
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

def get_batchdividend(tickers):
    # get months dividend list to make sure won't miss anyone
    url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols={}&types=dividends&range=6m'.format(','.join(tickers))
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

def get_batchsplit(tickers):
    # get months dividend list to make sure won't miss anyone
    url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols={}&types=splits&range=6m'.format(','.join(tickers))
    #stk = requests.get(url)
    stk = httphelper.get_httprequest(url)
    return stk.json()

