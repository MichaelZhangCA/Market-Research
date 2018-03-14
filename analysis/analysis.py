from crossreference import *

from codetimer import CodeTimer
from johncarter_study import jcsqueeze, jcsqueeze_chart

def process_jc_study(symbol):
   
    with CodeTimer('Prepare JC Squeeze data') as ct:
        df = jcsqueeze.process_jcsqueeze(symbol)

    # draw chart
    jcsqueeze_chart.drawchart(symbol, df)
    

if (__name__ == '__main__'):
    johncarter_study('MSFT')