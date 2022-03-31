import logging
import threading
import time
import apihandler


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
        actual_trend = True
      else:
        actual_trend = False
      
      # calcolo trend passato
      if ema_fast[-2] > ema_slow[-2]:
        last_trend = True
      else:
        last_trend = False
      
      logging.info(actual_trend)
      print(ema_fast[-1])
      print(ema_slow[-1])
      # controllo se il trend cambia
      if last_trend != actual_trend:
        logging.info("EMA TRADER")
        
        
        apihandler.close_for_symbol(self.symbol)
        if actual_trend:
          apihandler.open_buy(self.symbol, 1)
        else:
          apihandler.open_sell(self.symbol, 1)

      time.sleep(timeframe[self.timeframe] * 60)
    