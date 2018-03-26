""" Load symbol list and pick parameter, then process JC data
    either output charts, or for ML data preparation
"""
from crossreference import *
from logger import Logger
from uihelper import UiHelper
from datarepository import symbolrepo, indexrepo, stockpricerepo
from analysisrepository import johncarterrepo as jcrepo
import appinit

from johncarter_study import jcsqueeze, jcsqueeze_chart as jcchart
from johncarter_study.jcsqueeze import DEFAULT_JC_PRAM
from johncarter_study.jcsqueeze_para import JcSqueeze_Para
from johncarter_study.jcsqueeze_chart import JcChartColor_Black, JcChartColor_White

def process_jc(symbols=None, jcpara=DEFAULT_JC_PRAM):
    #para = JcSqueeze_Para('ATR KC - PPO Trend')
    #para.kc_para.atr_mode = 'atr'
    #para.trend_indicator = 'PPO'
    #para.wave_para.indicator = 'PPO'
    #para.wave_para.shortperiod = 55
    #para.wave_para.shortperiod = 144
    #para.wave_para.shortperiod = 377
    print('==> processing...')
    with Logger("Proceee JC Squeeze") as log:

        if (symbols == None):
            log.loginfo("==> load symbol list")
            indexsymbols = indexrepo.get_indexsymbollist()
            # convert to symbol list only
            symbols = [row[0] for row in indexsymbols]

        if (len(symbols) == 0):
            log.logwarning(' -? There is no symbol to process')
            pring(' =? no symbol found')
            return

        cnt = 0
        log.loginfo(' -| Start process JC squeeze')

        jcrepo.update_jcpara(jcpara)

        with UiHelper(len(symbols)) as ui:
            for sym in symbols:
                log.loginfo(' -> start process jc for {}'.format(sym))

                # load stock price
                df = stockpricerepo.get_stock_adjprice(sym)
                if(df.empty):
                    log.logwarning(' -? has no price data for {}'.format(sym))
                else:
                    df_jc = jcsqueeze.process_jcsqueeze(sym, df, jcpara)
                    # call chart but won't open the chart
                    df_jc = df_jc.dropna()

                    if(df_jc.empty):
                        log.logwarning(" -? {} doesn't have enough history for JC squeeze chart".format(sym))
                    else:
                        jcchart.drawchart(sym, df_jc, jcpara, theme = JcChartColor_White(), auto_open_chart=False)
                        # save to database
                        jcrepo.refresh_jcdata(sym, df_jc, jcpara)
                
                ui.performstep()


        log.loginfo(' =| JC process completed')
        print(' =| JC process completed')
    # end of process
    return


if (__name__ == '__main__'):
    appinit.app_init()
    
    para = JcSqueeze_Para('14 EMATR')
    #para.kc_para.atr_mode = 'atr'
    #para.kc_para.atr_period = 10
    #para.trend_indicator = 'PPO'
    #para.wave_para.indicator = 'PPO'
    #para.wave_para.shortperiod = 55
    #para.wave_para.shortperiod = 144
    #para.wave_para.shortperiod = 377


    process_jc(['WYNN'], para)