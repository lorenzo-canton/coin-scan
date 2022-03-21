# D261324228
# jQ8sw
# f8b1b32250896804e7398ce31a2106dee70e4eef

import logging
import threading
import time
import strat.emastrat as strat
from socket import SocketIO, socket
from numpy import number
import pandas as pd
import datetime as dt
import fxcmpy

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

TOKEN = 'f8b1b32250896804e7398ce31a2106dee70e4eef'


timeframe = {
    'm1' : 1,
    'm5' : 5,
    'm15' : 15,
    'h1' : 60,
    'h2' : 2 * 60,
    'h3' : 3 * 60,
    'h4' : 4 * 60,
    'h6' : 6 * 60,
    'h8' : 8 * 60,
    'D1' : 24 * 60,
    'W1' : 7 * 24 * 60,
    'M1' : 30 * 24 * 60
}


def get_data(con):
    return con.get_candles('GBP/JPY', period='D1', number=20)


def thread_function(name, con, tf):
    con.logger.disabled = True
    while True:
        logging.info("Thread %s", name)
        logging.info('\n' + get_data(con))
        time.sleep(timeframe[tf] * 60)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', log_file=None)
    con.logger.disabled = True
    traders = [
        {
            'target' : thread_function,
            'name' : 'api',
            'tf' : 'm1'
        }
    ]

    for i in traders:
        x = threading.Thread(target=i['target'], args=(i['name'], con, i['tf'],))
        x.start()
