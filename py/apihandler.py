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


def get_orders():
    return con.get_open_positions()


def get_open_orders_id():
    return con.get_open_trade_ids()

def open_trade(sym, is_buy, amount, timef, rate, is_in_pips, limit, at_market, stop, trailing_step):
    con.open_trade(sym, is_buy, amount, timef, 'AtMarket', rate, is_in_pips, limit, at_market, stop, trailing_step)

def open_buy(sym, amt):
    con.create_market_buy_order(sym, amt)


def open_sell(sym, amt):
    con.create_market_sell_order(sym, amt)


def close_order(id, amt):
    con.close_trade(id, amt)


def close_for_symbol(sym):
    con.close_all_for_symbol(sym)