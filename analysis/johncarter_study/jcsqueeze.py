import pandas as pd

# cross reference
from datarepository import stockpricerepo
from indicator import trend_indicator as trendidc, volatility_indicator as volidc
from .jcsqueeze_para import JcSqueeze_Para

# default JC parameters
DEFAULT_JC_PRAM = JcSqueeze_Para()
'''
DEFAULT_JC_PRAM = {
    'sma_period':20,
    'dev_mode':'std',
    'ema_period':20,
    'atr_mode':'atr',
    'atr_period':14,
    'macd':'12/26/9',
    'wavebase':8,
    'wavea':34,
    'waveb':89,
    'wavec':233
    }
'''

""" Live calcualte John Carter TTM Squeeze indicator based on full history adjusted price
"""
def process_jcsqueeze(symbol, df, jcpara=DEFAULT_JC_PRAM):

  
    # live calculate Bollings Band
    sma, stdev, smpldev = trendidc.process_sma(df.adj_close, jcpara.bb_para.sma_period)
    df['bb_middle'] = sma
    if (jcpara.bb_para.dev_mode == 'std'):
        df['bb_upper'] = sma + stdev * 2
        df['bb_lower'] = sma - stdev * 2
    else:
        df['bb_upper'] = sma + smpldev * 2
        df['bb_lower'] = sma - smpldev * 2
    
    # Keltner Channel
    ema = trendidc.process_ema(df.adj_close, jcpara.kc_para.ema_period)
    df['kc_middle'] = ema
    if (jcpara.kc_para.atr_mode=='atr'):
        atr = volidc.process_atr(df, jcpara.kc_para.atr_period)
        df['kc_upper'] = ema + atr * 2
        df['kc_lower'] = ema - atr * 2
    else:
        ematr = volidc.process_ematr(df, jcpara.kc_para.atr_period)
        df['kc_upper'] = ema + ematr * 2
        df['kc_lower'] = ema - ematr * 2

    # MACD
    trend_periods = jcpara.trend_period.split('/')
    emashort = trendidc.process_ema(df.adj_close, int(trend_periods[0]))
    emalong = trendidc.process_ema(df.adj_close, int(trend_periods[1]))
    if (jcpara.trend_indicator == 'MACD'):
        df['trend'] = trendidc.process_macd(emashort, emalong, int(trend_periods[2]))
    else:
        df['trend'] = trendidc.process_ppo(emashort, emalong, int(trend_periods[2]))

    # WAVE A/B/C
    emabase = trendidc.process_ema(df.adj_close, jcpara.wave_para.baseperiod)
    emawavea = trendidc.process_ema(df.adj_close, jcpara.wave_para.shortperiod)
    emawaveb = trendidc.process_ema(df.adj_close, jcpara.wave_para.mediumperiod)
    emawavec = trendidc.process_ema(df.adj_close, jcpara.wave_para.longperiod)

    if (jcpara.wave_para.indicator=="MACD"):
        df['wavea'] = trendidc.process_macd(emabase, emawavea, jcpara.wave_para.shortperiod)
        df['waveb'] = trendidc.process_macd(emabase, emawavea, jcpara.wave_para.mediumperiod)
        df['wavec'] = trendidc.process_macd(emabase, emawavea, jcpara.wave_para.longperiod)
    else:
        df['wavea'] = trendidc.process_ppo(emabase, emawavea, jcpara.wave_para.shortperiod)
        df['waveb'] = trendidc.process_ppo(emabase, emawavea, jcpara.wave_para.mediumperiod)
        df['wavec'] = trendidc.process_ppo(emabase, emawavea, jcpara.wave_para.longperiod)

    return df
    pass


