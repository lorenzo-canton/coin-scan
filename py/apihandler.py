import logging
import fxcmpy
import time
from socket import SocketIO, socket

from ENV import TOKEN

def init():
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
    global con
    con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', log_file=None)
    con.logger.disabled = True

def get_data(sym, per, num):
    return con.get_candles(sym, period=per, number=num)
