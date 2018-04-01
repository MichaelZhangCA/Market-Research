import httphelper
import requests
import quandl, pandas as pd

quandl_partialurl = 'https://www.quandl.com/api/v3/datasets/WIKI/{}/data.json?start_date={}&api_key={}'
quandl_fullurl = 'https://www.quandl.com/api/v3/datasets/WIKI/{}/data.json?&api_key={}'

def load_historicdata(symbol):
    url = quandl_fullurl.format(symbol, quandl.ApiConfig.api_key)
    return __process_request(url)

def load_partialhistoricdata(symbol, startdate):
    url = quandl_partialurl.format(symbol, startdate.strftime('%Y-%m-%d'), quandl.ApiConfig.api_key)
    # print(url)
    return __process_request(url)


def __process_request(url):

    #jsn = requests.get(url).json()
    jsn = httphelper.get_httprequest(url).json()

    data = jsn['dataset_data']['data']
    cln = jsn['dataset_data']['column_names']
    df = pd.DataFrame(data = data, columns = cln)
    df.set_index('Date', inplace=True)
    df.index = df.index.astype('M')
    df = df.sort_index()

    return df