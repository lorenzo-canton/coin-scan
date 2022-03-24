import logging
import threading
import time


from apihandler import get_data
from ENV import timeframe, ema_fast_number


class EmaTrader(threading.Thread):

  def ema(self, close, last):
    return (close - last) * (self.alpha + last)
  
  def __init__(self, symbol, timeframe):
    threading.Thread.__init__(self)
    log_format = "%(asctime)s: %(message)s"
    self.symbol = symbol
    self.timeframe = timeframe
    self.alpha = 2/(5+1)
    
  def run(self):
    while True:
      logging.info("EMA TRADER")
      df = get_data(self.symbol, self.timeframe, ema_fast_number)

      #ema_fast = df['askclose'].mean()
      #df['mva_fast'] = df['askclose'].ewm(span=ema_fast_number)
      ema10 = df['bidclose'].ewm(span=10).mean()
      print(ema10)



      time.sleep(timeframe[self.timeframe] * 60)
    