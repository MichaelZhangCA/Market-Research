import datetime
import numpy as np
import pandas as pd

from repobase import MysqlConnection
import appvariable as appvar

"""
# get ajusted price data by symbol and given start date. the result will include start date.
# caller should calculate for the start accurately since it will impact further calculation in some indicators. ex. EMA
# Some indicators like SMA will need load back more than {Period} business days for calculation
"""
def get_stock_adjprice(symbol, startdate=appvar.STOCK_START_DATE):

    query = ("SELECT effective_date, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_volume` FROM `market.stock_price` "
             "WHERE symbol = '{0}' and effective_date >= '{1}' order by effective_date".format(symbol, startdate.strftime('%Y-%m-%d')))

    with MysqlConnection() as cnx:
        cur = cnx.cursor()
        cur.execute(query)

        #df = pd.DataFrame(cur.fetchall(), dtype=np.float)
        df = pd.DataFrame(cur.fetchall())

        if (not df.empty):
            df.columns = cur.column_names
            df.set_index('effective_date', inplace=True)

        cur.close()
         
        return df


""" Function to update stock price
    refresh price will drop all exists rows and refresh the whol history
    patch only drop any duplicated exist rows and insert new rows
"""
def __get_insert_sql(symbol):
    ins =("INSERT INTO `stock_market`.`market.stock_price` "
        "(`symbol`,`effective_date`,`open`,`high`,`low`,`close`,`volume`,`ex_dividend`,`split_ratio`,`adj_open`,`adj_high`,`adj_low`,`adj_close`,`adj_volume`) "
        "VALUES "
        "('{0}','{1}',%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Ex-Dividend)s,%(Split Ratio)s,%(Adj. Open)s,%(Adj. High)s,%(Adj. Low)s,%(Adj. Close)s,%(Adj. Volume)s)"
        .format(symbol, "{}"))
    return ins

def refresh_symbolhistoric(symbol, hisdata):
    
    if (hisdata.empty):
        return

    clr = "DELETE FROM `market.stock_price` WHERE symbol = '{}'".format(symbol)

    ins = __get_insert_sql(symbol)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # clear current record
        cur.execute(clr)
        cnx.commit()

        hisdic = hisdata.to_dict(orient='index')

        # insert from the list
        for ts, row in hisdic.items():
            # put effective date to query
            query = ins.format(ts.to_pydatetime().strftime('%Y-%m-%d'))
            cur.execute(query, row)
            
        cnx.commit()
        cur.close()

def patch_symbolhistoric(symbol, hisdata):
    
    if (hisdata.empty):
        return

    # get earliest date in the patch dataset
    firstdate = hisdata.index.min()
    # print("  : will clean up data after (and equal) {0}".format(firstdate.to_pydatetime().strftime('%Y-%m-%d')))

    clr = "DELETE FROM `market.stock_price` WHERE symbol = '{0}' and effective_date >= '{1}'".format(symbol, firstdate.strftime('%Y-%m-%d'))
    # print("  : sql : {}".format(clr))

    ins = __get_insert_sql(symbol)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # clear current record
        cur.execute(clr)
        cnx.commit()

        hisdic = hisdata.to_dict(orient='index')

        # insert from the list
        for ts, row in hisdic.items():
            # put effective date to query
            query = ins.format(ts.to_pydatetime().strftime('%Y-%m-%d'))
            cur.execute(query, row)
            pass

        cnx.commit()
        cur.close()

        
def clear_symbol_price(symbol):
    clr = "DELETE FROM `market.stock_price` WHERE symbol = '{0}'".format(symbol)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()
        cur.execute(clr)
        cnx.commit()
