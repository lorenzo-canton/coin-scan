# D261324228
# jQ8sw
# 546a088987e0e775aa7834095f187d3b1c4e4e06

import logging

import pandas as pd
import apihandler
import ENV
from emastrat import EmaTrader

from http.server import HTTPServer
from server import Serv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# apihandler.connect()


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # trader1 = ENV.trader[0]
    # ema_trader = EmaTrader(trader1)
    # ema_trader.start()


    httpd = HTTPServer(('localhost', 8080), Serv)
    httpd.serve_forever()
    
