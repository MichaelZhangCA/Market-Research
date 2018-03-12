
class BollingsBand_Para(object):

    @property
    def sma_period(self):
        return self._sma_period

    @sma_period.setter
    def sma_period(self, val):
        self._sma_period = val

    # deviation could be std / smpl
    @property
    def dev_mode(self):
        return self._dev_mode

    @dev_mode.setter
    def dev_mode(self, val):
        self._dev_mode = val

    pass

class KeltnerChannel_Para(object):

    @property
    def ema_period(self):
        return self._ema_period

    @ema_period.setter
    def ema_period(self, val):
        self._ema_period = val

    @property
    def atr_period(self):
        return self._atr_period

    @atr_period.setter
    def atr_period(self, val):
        self._atr_period = val

    # atr mode could be 'atr' or 'ematr'
    @property
    def atr_mode(self):
        return self._atr_mode

    @atr_mode.setter
    def atr_mode(self, val):
        self._atr_mode = val

    pass


class TTM_Wave_Para(object):

     # wave could be MACD or PPO
    @property
    def indicator(self):
        return self._indicator

    @indicator.setter
    def indicator(self, val):
        self._indicator = val

    @property
    def baseperiod(self):
        return self._baseperiod

    @baseperiod.setter
    def baseperiod(self, val):
        self._baseperiod = val

    @property
    def shortperiod(self):
        return self._shortperiod

    @shortperiod.setter
    def shortperiod(self, val):
        self._shortperiod = val

    @property
    def mediumperiod(self):
        return self._mediumperiod

    @mediumperiod.setter
    def mediumperiod(self, val):
        self._mediumperiod = val

    @property
    def longperiod(self):
        return self._longperiod

    @longperiod.setter
    def longperiod(self, val):
        self._longperiod = val

    pass

class JcSqueeze_Para(object):

    def __init__(self, paraname = 'Default',  **kwargs):

        ''' Return a default JohnCarter Squeeze parameter
        '''
        self._paraname = paraname

        bbpara = BollingsBand_Para()
        bbpara.sma_period = 20
        bbpara.dev_mode = 'std'     # 'smpl'
        self._bb_para = bbpara

        kcpara = KeltnerChannel_Para()
        kcpara.ema_period = 20
        kcpara.atr_period = 14
        kcpara.atr_mode = 'ematr'   # 'atr'
        self._kc_para = kcpara

        self._trend_indicator = 'MACD'
        self._trend_period = '12/26/9'

        wavepara = TTM_Wave_Para()
        wavepara.indicator = 'MACD'
        wavepara.baseperiod = 8
        wavepara.shortperiod = 34
        wavepara.mediumperiod = 89
        wavepara.longperiod = 233

        self._wave_para = wavepara

        return super().__init__(**kwargs)

    @property
    def paraname(self):
        return self._paraname

    @paraname.setter
    def paraname(self, val):
        self._paraname = val

    @property
    def bb_para(self):
        return self._bb_para

    @bb_para.setter
    def bb_para(self, val):
        self._bb_para = val

    @property
    def kc_para(self):
        return self._kc_para

    @kc_para.setter
    def kc_para(self, val):
        self._kc_para = val

    # either MACD or PPO
    @property
    def trend_indicator(self):
        return self._trend_indicator

    @trend_indicator.setter
    def trend_indicator(self, val):
        self._trend_indicator = val

    # short/long/signal period for MACD/PPO (default: 12/26/9)
    @property
    def trend_period(self):
        return self._trend_period

    @trend_period.setter
    def trend_period(self, val):
        self._trend_period = val

    @property
    def wave_para(self):
        return self._wave_para

    @wave_para.setter
    def wave_para(self, val):
        self._wave_para = val

    pass



