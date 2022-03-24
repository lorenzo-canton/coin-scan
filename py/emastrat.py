import logging
import threading
import time


from apihandler import get_data
from ENV import timeframe, ema_fast_number, ema_slow_number


class EmaTrader(threading.Thread):
  
  def __init__(self, symbol, timeframe):
    threading.Thread.__init__(self)
    self.symbol = symbol
    self.timeframe = timeframe
    
    
  def run(self):
    while True:
      
      df = get_data(self.symbol, self.timeframe, ema_slow_number)

      # calcolo ema veloce e lenta
      ema_fast = df['bidclose'].ewm(span=ema_fast_number).mean()
      ema_slow = df['bidclose'].ewm(span=ema_slow_number).mean()
      
      # calcolo trend attuale
      if ema_fast[-1] > ema_slow[-1]:
        actual_trend = 'up'
      else:
        actual_trend = 'down'
      
      # calcolo trend passato
      if ema_fast[-2] > ema_slow[-2]:
        last_trend = 'up'
      else:
        last_trend = 'down'
      
      # controllo se il trend cambia
      if last_trend != actual_trend:
        logging.info("EMA TRADER")
        logging.info(actual_trend)

      time.sleep(timeframe[self.timeframe] * 60)
    