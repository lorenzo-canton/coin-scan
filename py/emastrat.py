import logging
import threading
import time
import apihandler


from apihandler import get_data
from ENV import timeframe


class EmaTrader(threading.Thread):
  
  def __init__(self, params):
    threading.Thread.__init__(self)
    self.params = params
    
    
  def run(self):
    while True:
      
      df = get_data(self.params["symbol"], self.params["timeframe"], self.params["ema_slow"])

      # calcolo ema veloce e lenta
      ema_fast = df['bidclose'].ewm(span=self.params["ema_fast"]).mean()
      ema_slow = df['bidclose'].ewm(span=self.params["ema_slow"]).mean()
      
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
      
      logging.info("EMA TRADER")
      print(actual_trend)
      print(ema_fast[-1])
      print(ema_slow[-1])
      
      # controllo se il trend cambia
      if last_trend != actual_trend:
        logging.info("NEW TRADE")
        
        apihandler.close_for_symbol(self.params["symbol"])
        
        if actual_trend:
          apihandler.open_buy(self.params["symbol"], 1)
        else:
          apihandler.open_sell(self.params["symbol"], 1)

      print()
      time.sleep(timeframe[self.params["timeframe"]] * 60)
    