# D261324228
# jQ8sw
# 546a088987e0e775aa7834095f187d3b1c4e4e06

import logging
import threading
import time
from socket import SocketIO, socket
from numpy import number
import pandas as pd
import datetime as dt
import fxcmpy

import apihandler
import ENV
from emastrat import EmaTrader

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
apihandler.connect()

if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

    trader1 = ENV.trader[0]
    ema_trader = EmaTrader(trader1)
    ema_trader.start()
