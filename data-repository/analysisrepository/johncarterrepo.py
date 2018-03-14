import datetime
from repobase import MysqlConnection

def update_jcpara(jcpara):

    update_para = "INSERT INTO `stock_market`.`study.jc_squeeze_para` \
                (`para_name`, `sma_period`, `dev_mode`, `ema_period`, `atr_period`, `atr_mode`, `trend_indicator`, `trend_period`, \
                `wave_indicator`, `wave_base_period`, `wave_short_period`, `wave_medium_period`, `wave_long_period`) \
                VALUES \
                (%(para_name)s, %(sma_period)s, %(dev_mode)s, %(ema_period)s, %(atr_period)s, %(atr_mode)s, %(trend_indicator)s, %(trend_period)s, \
                %(wave_indicator)s, %(wave_base_period)s, %(wave_short_period)s, %(wave_medium_period)s, %(wave_long_period)s) \
                ON DUPLICATE KEY UPDATE \
                `para_name`=%(para_name)s, `sma_period`=%(sma_period)s, `dev_mode`=%(dev_mode)s, `ema_period`=%(ema_period)s, `atr_period`=%(atr_period)s, \
                `atr_mode`=%(atr_mode)s, `trend_indicator`=%(trend_indicator)s, `trend_period`=%(trend_period)s, `wave_indicator`=%(wave_indicator)s, \
                `wave_base_period`=%(wave_base_period)s, `wave_short_period`=%(wave_short_period)s, `wave_medium_period`=%(wave_medium_period)s, `wave_long_period`=%(wave_long_period)s"

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # update/insert para table
        cur.execute(update_para, jcpara.asdict())
        cnx.commit()
        cur.close()

def refresh_jcdata(symbol, jcdata, jcpara):

    ins = "INSERT INTO `study.jc_squeeze` (`para_name`, `symbol`, `effective_date`, \
          `bb_middle`, `bb_upper`, `bb_lower`, `kc_middle`, `kc_upper`, `kc_lower`, `trend`, `wavea`, `waveb`, `wavec`) \
          VALUES ('{}', '{}', '{}', \
          %(bb_middle)s, %(bb_upper)s, %(bb_lower)s, %(kc_middle)s, %(kc_upper)s, %(kc_lower)s, %(trend)s, %(wavea)s, %(waveb)s, %(wavec)s)" \
          .format(jcpara.paraname, symbol, '{}')

    clr = "DELETE FROM `study.jc_squeeze` WHERE symbol='{}' and `para_name`='{}'".format(symbol, jcpara.paraname)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # clear current record
        cur.execute(clr)
        cnx.commit()

        # insert from the list
        jc = jcdata.to_dict(orient='index')
        for idx, row in jc.items():
            # put effective date to query
            query = ins.format(idx.strftime('%Y-%m-%d'))
            cur.execute(query, row)
            pass
                
        cnx.commit()
        cur.close()

    pass

