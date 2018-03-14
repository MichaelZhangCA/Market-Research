import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
from datetime import timedelta

# the folder for all output
_chart_output_folder = 'charts'

class JcChartColor(object):
    bb = 'rgb(91, 154, 255)'
    kc = 'rgb(244, 118, 73)'
    candle_up = '#586b59'
    candle_down = '#51150e'

    squeeze_on = '#022ff7'
    squeeze_off = '#404241'  #f21104 for red
    squeeze_line = 'rgb(30,60,30)'

    trend_up_pos = '#0599b7'
    trend_down_pos = '#029107'
    trend_up_neg = '#871001'
    trend_down_neg = '#d35004'

    wave_up = '#029107'
    wave_down = '#871001'
    pass

def drawchart(symbol, df, para, auto_open_chart=True):

    # find the last 6 month as x axis range
    range_enddate = df.index.max()
    range_startdate = range_enddate + timedelta(weeks=-36)

    # only keep recent 3 years rows
    df = df.drop(df[df.index < range_enddate + timedelta(weeks=-160) ].index)
    
    # get some label information from parameter
    _lbl_chart_title = 'John Carter Squeeze Chart [ {} ]'.format(para.paraname)
    _lbl_trend_idc_name = para.trend_indicator
    _lbl_trend_idc_pop = "{}({})".format(para.trend_indicator, para.trend_period)
    _lbl_wavea_pop = '{0}({1}/{2}/{2})'.format(para.wave_para.indicator, para.wave_para.baseperiod, para.wave_para.shortperiod)
    _lbl_waveb_pop = '{0}({1}/{2}/{2})'.format(para.wave_para.indicator, para.wave_para.baseperiod, para.wave_para.mediumperiod)
    _lbl_wavec_pop = '{0}({1}/{2}/{2})'.format(para.wave_para.indicator, para.wave_para.baseperiod, para.wave_para.longperiod)

    _lbl_bb_upper = 'Bollinger Bands'
    _lbl_bb_lower = '{} SMA 2 * {} deviation'.format(para.bb_para.sma_period, ('standard' if (para.bb_para.dev_mode=='std') else 'sample'))
    _lbl_kc_upper = 'Keltner Channel'
    _lbl_kc_lower = '{} EMA 2 * {} {}'.format(para.kc_para.ema_period, para.kc_para.atr_period, para.kc_para.atr_mode)

    # enrich the data - trend indecator up/down, bb_low > kc_low, bb_high < kc_high
    df['trend_up'] = df.trend > df.trend.shift(-1)
    df['squeeze_value'] = 0                                                             # squeeze value set to 0 to show the marker on zero line
    df['is_squeeze'] = (df.bb_lower >= df.kc_lower) & (df.bb_upper <= df.kc_upper)     # squeeze indicator for color
    df['squeeze_line'] = (df.is_squeeze == False) & (df.is_squeeze.shift(1) == True)

    # color definition
    '''
    _color_bb = 'rgb(91, 154, 255)'
    _color_kc = 'rgb(244, 118, 73)'
    _color_candle_up = '#586b59'
    _color_candle_down = '#51150e'
    '''

    # define style of Bollinger bands & Keltner Channels
    _style_bb_band = dict( color = JcChartColor.bb, width = 1, dash = 'line')
    _style_bb_middle = dict( color = JcChartColor.bb, width = 1, dash = 'dot')

    _styl_kc_band = dict( color = JcChartColor.kc, width = 1, dash = 'line')
    _styl_kc_middle = dict( color = JcChartColor.kc, width = 1, dash = 'dot')

    '''
    style_bollingerbands_middle = dict( color = ('rgb(22, 96, 167)'), width = 1, dash = 'dot')
    style_bollingerbands_upper = dict( color = ('rgb(22, 96, 167)'), width = 1, dash = 'line')
    style_bollingerbands_lower = dict( color = ('rgb(91, 154, 255)'), width = 1, dash = 'line')

    style_kc_middle = dict( color = ('rgb(247, 94, 39)'), width = 1, dash = 'dot')
    style_kc_upper = dict( color = ('rgb(247, 94, 39)'), width = 1, dash = 'line')
    style_kc_lower = dict( color = ('rgb(244, 118, 73)'), width = 1, dash = 'line')
    '''

    trace_candle = go.Candlestick(x=df.index, open=df.adj_open, high=df.adj_high, low=df.adj_low, close=df.adj_close, 
                        showlegend=False, name='close price',
                        increasing=dict(line=dict(color= JcChartColor.candle_up)), #b1e2b6
                        decreasing=dict(line=dict(color= JcChartColor.candle_down))
                        ,hoverinfo='y'
                    )

    '''
    # OHLC chart for stock price, hide hover info to make UI more readable
    trace_ohlc = go.Ohlc(x=df.index, open=df.adj_open, high=df.adj_high, low=df.adj_low, close=df.adj_close, 
                         showlegend=False, name='close price',
                         increasing=dict(line=dict(color= '#b1e2b6')),
                         decreasing=dict(line=dict(color= '#51150e')),
                         hoverinfo='none'
                        )
    '''

    trace_bb_middle = go.Scatter(x=df.index, y=df.bb_middle, name='BB Middle', legendgroup='Bollinger Bands',
                                 showlegend=False, opacity=0.5, hoverinfo='none',
                                 line = _style_bb_middle
                                )
    trace_bb_upper = go.Scatter(x=df.index, y=df.bb_upper, name=_lbl_bb_upper, legendgroup='Bollinger Bands',
                                line = _style_bb_band
                               )
    trace_bb_lower = go.Scatter(x=df.index, y=df.bb_lower, name=_lbl_bb_lower, legendgroup='Bollinger Bands',
                                line = _style_bb_band
                               )
    
    trace_kc_middle = go.Scatter(x=df.index, y=df.kc_middle, name='KC Middle', legendgroup='Keltner Channels 2ATR',
                                 showlegend=False, opacity=0.5, hoverinfo='none',
                                 line = _styl_kc_middle
                                )
    trace_kc_upper = go.Scatter(x=df.index, y=df.kc_upper, name=_lbl_kc_upper, legendgroup='Keltner Channels 2ATR',
                                     line = _styl_kc_band
                                    )
    trace_kc_lower = go.Scatter(x=df.index, y=df.kc_lower, name=_lbl_kc_lower, legendgroup='Keltner Channels 2ATR',
                                     line = _styl_kc_band
                                    )
    '''
    # create volume bar chart on the bottom
    tarce_volume = go.Bar(x=df.index, y=df.adj_volume, name='volume', showlegend=False, marker=dict(color='rgb(87, 91, 130)'),
                          yaxis = 'y2'
                         )
    '''

    # color dict for trend indicator, either MACD or PPO
    trend_colordict = []
    squeeze_colordict = []
    for index, row in df.iterrows():
        # MACD/PPO
        '''
        color_trend = '#029107' if (row['trend']>=0 and row['trend_up']==True) else \
                    ('#0599b7' if (row['trend']>=0 and row['trend_up']==False) else \
                    ('#871001' if (row['trend']<0 and row['trend_up']==False) else '#d35004' ))
        '''
        color_trend = JcChartColor.trend_up_pos if (row['trend']>=0 and row['trend_up']==True) else \
                     (JcChartColor.trend_down_pos if (row['trend']>=0 and row['trend_up']==False) else \
                     (JcChartColor.trend_down_neg if (row['trend']<0 and row['trend_up']==False) else JcChartColor.trend_up_neg ))

        trend_colordict.append(color_trend)
        # squeeze
        color_squeeze = JcChartColor.squeeze_on if row['is_squeeze'] else JcChartColor.squeeze_off  #f21104 for red
        squeeze_colordict.append(color_squeeze)


    trace_trend = go.Bar(x=df.index, y=df.trend, name=_lbl_trend_idc_pop, showlegend=False, 
                        marker=dict(color=trend_colordict),
                        yaxis = 'y3'
                       )

    trace_squeeze = go.Scatter(x=df.index, y=df.squeeze_value, name='', showlegend=False, 
                               mode = 'markers', marker=dict(size=6, color=squeeze_colordict), hoverinfo='none',
                               yaxis = 'y3'
                               )

    trace_wave_a = go.Bar(x=df.index, y=df.wavea, name=_lbl_wavea_pop, showlegend=False, 
                    marker=dict(color=[JcChartColor.wave_up if val>=0 else JcChartColor.wave_down for val in df.wavea]),
                    yaxis = 'y4'
                   )

    trace_wave_b = go.Bar(x=df.index, y=df.waveb, name=_lbl_waveb_pop, showlegend=False, 
                marker=dict(color=[JcChartColor.wave_up if val>=0 else JcChartColor.wave_down for val in df.waveb]),
                yaxis = 'y5'
               )
    trace_wave_c = go.Bar(x=df.index, y=df.wavec, name=_lbl_wavec_pop, showlegend=False, 
                    marker=dict(color=[JcChartColor.wave_up if val>=0 else JcChartColor.wave_down for val in df.wavec]),
                    yaxis = 'y6'
                   )

    # collect all traces show on the chart
    data = [trace_candle, trace_bb_middle, trace_kc_middle,
            trace_bb_upper, trace_bb_lower, trace_kc_upper, trace_kc_lower, 
            #tarce_volume, 
            trace_trend, trace_squeeze, trace_wave_a, trace_wave_b, trace_wave_c]
    

    # find the min & max in the range
    y_range_high = int(df[df.index > range_startdate].adj_close.max() / 10 +1 ) * 10
    y_range_low = int( df[df.index > range_startdate].adj_close.min() / 10 ) * 10

    # print(y_range_high, y_range_low)

    # fixrange=True, cannot zoom in, useful for y axis for the small indicators
    # fixrange=Fasle with range setting, used in the main chart so it could be zoomed in
    # define xaxis template to shorten layout
    xaxis_template = dict(type="date", showgrid=True, zeroline=True, showline=True, 
                          rangeslider=dict(visible=False), fixedrange=False, autorange=False,
                          range = [range_startdate, range_enddate]
                     )

    # generate shapes for squeeze line
    squeezeline_style = {'color':JcChartColor.squeeze_line, 'width':1, 'dash':'dot'}
    
    squeezelines = []
    dflines = df[df.squeeze_line==True]
    for idx, row in dflines.iterrows():
        squeezeline = {'type':'line', 'y0':0, 'y1':1, 'xref':'x', 'yref':'paper', 'line':squeezeline_style}
        squeezeline['x0'] = squeezeline['x1'] = idx.strftime('%Y-%m-%d')
        squeezelines.append(squeezeline)
    
    layout = go.Layout(
        title = '{} - {}'.format(symbol, _lbl_chart_title),
        # put legend in left/top coner
        legend = dict(x=0.05, y=1.0),
        height=1050,
        margin = go.Margin(l=80,r=30,t=50,b=100),
        paper_bgcolor='#000', plot_bgcolor='#000',

        xaxis = xaxis_template,

        # all yaxis domains (leave gap between y and below to show the x axis labels
        yaxis = dict(domain=[0.35,1], fixedrange=False, range=[y_range_low, y_range_high], autorange=False ),
        # yaxis2 = dict(domain=[0.5,0.5], visible=False),
        yaxis3 = dict(domain=[0.225,0.325], fixedrange=True, title=_lbl_trend_idc_name),
        yaxis4 = dict(domain=[0.15,0.225], fixedrange=True, visible=True, title="WAVEA"),
        yaxis5 = dict(domain=[0.075,0.15], fixedrange=True, visible=True, title="WAVEB"),
        yaxis6 = dict(domain=[0,0.075], fixedrange=True, visible=True, title="WAVEC"),
        
        shapes = squeezelines
    )

    # control model bar    
    config = {'showLink':False, 'modeBarButtonsToRemove': ['sendDataToCloud','zoom2d','select2d','lasso2d']}
    
    fig = go.Figure(data=data, layout=layout )

    # output file name
    file_name = os.path.join(os.path.dirname(__file__), "{}\\{} - {}.html".format(_chart_output_folder, symbol, _lbl_chart_title))

    # standalone chart
    plotly.offline.plot(fig, filename=file_name, auto_open=auto_open_chart, config=config)



