import sys
import json

from iex import iexapi
from datarepository import indexrepo, symbolrepo, stockpricerepo as pricerepo, dividendrepo, splitrepo
import marketindex
from marketindex import MarketIndices
import quandlwrap
import mysql.connector

# import from core project
import datehelper
from logger import Logger
from uihelper import UiHelper


# service name for logging
service_name = "Market data loading service"

def process_symbollist():

    with Logger('Process symbol list') as log:
        log.loginfo ('==> start loading symbol list from IEX api')
        symbols = iexapi.get_referencedata()
        log.loginfo (' -> dumped list from IEX')
        symbolrepo.addsymbol(symbols)
        log.loginfo (' -| symbols list updated')

def process_companyinfo():

    with Logger('Process company info') as log:

        log.loginfo ('==> start updating symbol company info from IEX api')
        tickers = symbolrepo.get_newtickerlist()
    
        if (len(tickers) > 0):

            log.loginfo ('--> start getting company info for {0} tickers'.format(len(tickers)))
            cmplist = []
            batchcount = 0
            for ticker in tickers:
                try:
                    cmp = iexapi.get_compaydata(ticker)
                    cmplist.append(cmp)
                    log.loginfo(" -> added company info of : {0}".format(ticker))
                except json.decoder.JSONDecodeError:
                    log.logwarning("  ? get error when reteriving cmopany info for : {0}".format(ticker))
    
                batchcount += 1
                # save batch each 100 symbols
                if (batchcount >= 100):

                    log.loginfo ('  : save batched company info')
                    symbolrepo.update_companyinfo(cmplist)
            
                    # reset counter
                    cmplist = []
                    batchcount =0

            # save company info
            if (batchcount>0):
                log.loginfo (' : save left over records')
                symbolrepo.update_companyinfo(cmplist)
        
            log.loginfo (' -| all new tickers have been updated')
        else:
            log.loginfo (' -| there is no new ticker to update')


def batchupdate_marketindices():

    with Logger('Process Index Constituent') as log:
        log.loginfo("==> start loading market indices data")

        __update_marketindices(MarketIndices.NASDAQ100)
        __update_marketindices(MarketIndices.SP500)
        __update_marketindices(MarketIndices.DOW30)
        __update_marketindices(MarketIndices.TSX60)

        log.loginfo(" -| market indices data refreshed")

def __update_marketindices(idx):

    with Logger('Process Index Constituent') as log:
    
        log.loginfo(" -> start loading {0}".format(idx.name))
        data = marketindex.load_indexsymbol(idx)
        indexrepo.refresh_symbol(idx.name, data)
        log.loginfo(" -> {0} refreshed".format(idx.name))


def process_symbol_historicprice():

    with Logger("Dump Historic Data") as log:
        log.loginfo("==> start refresh historic data")
        symbols = indexrepo.get_indexsymbollist()

        with UiHelper(len(symbols)) as ui:
            for row in symbols:
                # only reload if latest date is no last business day
                tbd1 = datehelper.get_tbd1()

                symbol = row[0]; lastdate = row[1]

                try:
                    if (lastdate is None):
                        # new symbol, download full history and dump to table
                        log.loginfo("--> start dump historic data from quandl for : {}".format(symbol))
                        his = quandlwrap.load_historicdata(symbol)
                        log.loginfo(" -> dump full historic data from quandl for : {}".format(symbol))
                        pricerepo.refresh_symbolhistoric(symbol, his)
                        log.loginfo(" -| Completed historic data dump to database for : {}".format(symbol))
                    elif (lastdate < tbd1):
                        log.loginfo("--> start dump historic data from quandl for : {}".format(symbol))
                        partialhis = quandlwrap.load_partialhistoricdata(symbol, datehelper.get_nextday(lastdate))
                        log.loginfo(" -> dump partial historic data from quandl for : {}".format(symbol))
                        pricerepo.patch_symbolhistoric(symbol, partialhis)
                        log.loginfo(" -| Completed patch missing history for : {}".format(symbol))
                    else:
                        # if symbol already up-to-date then skip
                        pass

                except mysql.connector.errors.DataError as err:
                    log.logerror(repr("  ! MySQL error : {0}".format(err.msg)))

                except:
                    log.logerror(repr("  ! Got error when dumping : {0}, error : {1}".format(symbol, sys.exc_info()[0])))

                #count_cur += 1
                ui.performstep()
    
    # end of function
    return


""" Refresh dividend list for last 6 month
"""
def process_dividend():

    with Logger("Process Dividend") as log:
        log.loginfo("==> load symbol list")
        symbols = indexrepo.get_indexsymbollist()

        if (len(symbols) == 0):
            log.logwarning(' -? There is no symbol to process')
            return

        log.loginfo(' -| Start refreshing dividend list')
        with UiHelper(len(symbols)) as ui:
            symbol_batch = []
            for sym in [row[0] for row in symbols]:
                # continue adding symbol to the list until hit 90
                if(len(symbol_batch) < 90):
                    symbol_batch.append(sym)
                else:
                    # go get divident for the batch then save to databaes
                    __process_batch_dividend(','.join(symbol_batch))
                    symbol_batch = []

                ui.performstep()

            # once out the loop, check if there is something left in the batch
            if (len(symbol_batch) > 0):
                __process_batch_dividend(','.join(symbol_batch))
        
        log.loginfo(' -| Dividend list refreshed')
    # end of process
    return

def __process_batch_dividend(symbol_batch):
    # grab dividends from IEX by call batch
    dvds = iexapi.get_batchdividend(','.join(symbol_batch))

    for key, val in dvds.items():
        dividendrepo.refresh_dividend(key, val['dividends'])
    

""" Refresh split list for last 6 month
"""
def process_split():

    with Logger("Process Split") as log:
        log.loginfo("==> load symbol list")
        symbols = indexrepo.get_indexsymbollist()

        if (len(symbols) == 0):
            log.logwarning(' -? There is no symbol to process')
            return

        log.loginfo(' -| Start refreshing split list')
        with UiHelper(len(symbols)) as ui:
            symbol_batch = []
            for sym in [row[0] for row in symbols]:
                # continue adding symbol to the list until hit 90
                if(len(symbol_batch) < 90):
                    symbol_batch.append(sym)
                else:
                    # go get divident for the batch then save to databaes
                    __process_batch_split(','.join(symbol_batch))
                    symbol_batch = []

                ui.performstep()

            # once out the loop, check if there is something left in the batch
            if (len(symbol_batch) > 0):
                __process_batch_split(','.join(symbol_batch))
        
        log.loginfo(' -| Dividend list refreshed')
    # end of process
    return

def __process_batch_split(symbol_batch):
    # grab dividends from IEX by call batch
    dvds = iexapi.get_batchsplit(','.join(symbol_batch))

    for key, val in dvds.items():
        splitrepo.refresh_split(key, val['splits'])


def main():
    # set database connection info
    # DbConnection.init_connection(serverName, databaseName, userName, password)
    
    # update the symbol list with latest data
     process_symbollist()
    # patch all new symbol's company data
    # process_companyinfo()

    # update market indicies
    # batchupdate_marketindices()
    # __update_marketindices(MarketIndices.SP500)

    # load index live symbol list
    # process_symbol_historicprice()

if (__name__ == '__main__'):
    main()
