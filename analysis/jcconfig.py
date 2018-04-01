from configobj import ConfigObj
from johncarter_study.jcsqueeze_para import JcSqueeze_Para

def load_config():

    config = ConfigObj('.\\jcconfig.ini')
    para = config['jcpara']

    jcpara = JcSqueeze_Para(para['para_name'])

    if ('sma_period' in para):
        jcpara.bb_para.sma_period = para['sma_period']
    if ('dev_mode' in para):
        jcpara.bb_para.dev_mode = para['dev_mode']

    if ('ema_period' in para):
        jcpara.kc_para.ema_period = para['ema_period']
    if ('atr_mode' in para):
        jcpara.kc_para.atr_mode = para['atr_mode']
    if ('atr_period' in para):
        jcpara.kc_para.atr_period = para['atr_period']

    if ('trend_indicator' in para):
        jcpara.trend_indicator = para['trend_indicator']
    if ('trend_period' in para):
        jcpara.trend_period = para['trend_period']

    if ('wave_indicator' in para):
        jcpara.wave_para.indicator = para['wave_indicator']
    if ('wave_base_period' in para):
        jcpara.wave_para.baseperiod = para['wave_base_period']
    if ('wave_short_period' in para):
        jcpara.wave_para.shortperiod = para['wave_short_period']
    if ('wave_medium_period' in para):
        jcpara.wave_para.mediumperiod = para['wave_medium_period']
    if ('wave_long_period' in para):
        jcpara.wave_para.longperiod = para['wave_long_period']

    return jcpara

