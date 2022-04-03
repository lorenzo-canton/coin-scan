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
  

  def set_params(self, params):
    self.params = params


  def calculate_ema(self, data):
    # calcolo ema veloce e lenta
    ema_fast = data['bidclose'].ewm(span=self.params["ema_fast"]).mean()
    ema_slow = data['bidclose'].ewm(span=self.params["ema_slow"]).mean()
    return ema_fast, ema_slow
  
  def get_trend(self, fast, slow):
    if fast > slow:
      return True
    return False

    
  def run(self):
    while True:
      
      df1 = get_data(self.params["symbol"], self.params["timeframe"], self.params["ema_slow"])

      ema_fast, ema_slow = self.calculate_ema(df1)

      # trend corto
      actual_trend = self.get_trend(ema_fast[-1], ema_slow[-1])
      last_trend = self.get_trend(ema_fast[-2], ema_slow[-2])
      
      logging.info("EMA TRADER")
      print(actual_trend)
      print(ema_fast[-1])
      print(ema_slow[-1])

      # controllo se il trend cambia
      if last_trend != actual_trend:
        logging.info("NEW TRADE")
        
        apihandler.close_for_symbol(self.params["symbol"])
        
        # se il trend corto è uguale al trend lungo
        if actual_trend == self.get_trend(self.calculate_ema(get_data(self.params["symbol"], self.params["outerTimeframe"], self.params["ema_slow"]))):
          if actual_trend:
            apihandler.open_buy(self.params["symbol"], 1)
          else:
            apihandler.open_sell(self.params["symbol"], 1)

      print()
      time.sleep(timeframe[self.params["timeframe"]] * 60)
    