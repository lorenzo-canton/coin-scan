import logging
import fxcmpy
import time
from socket import SocketIO, socket

from ENV import TOKEN

def connect():
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
    global con
    con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', log_file=None)
    con.logger.disabled = True

def get_data(sym, per, num):
    return con.get_candles(sym, period=per, number=num)


def get_open(id):
    return con.get_open_position(id)


def get_order(id):
    return con.get_order(id)


def get_open_orders_id():
    return con.get_open_trade_ids()


def open_buy(sym, amt):
    con.create_market_buy_order(sym, amt)


def open_sell(sym, amt):
    con.create_market_sell_order(sym, amt)


def close_order(id, amt):
    con.close_trade(id, amt)