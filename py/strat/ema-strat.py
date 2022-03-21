# D261324228
# jQ8sw
# f8b1b32250896804e7398ce31a2106dee70e4eef
from socket import SocketIO, socket
from numpy import number
import pandas as pd
import json
import requests
import socket
import datetime as dt
import fxcmpy

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print('started')

TOKEN = 'f8b1b32250896804e7398ce31a2106dee70e4eef'

con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error')

df = con.get_candles('GBP/JPY', period='D1', number=20)

print(df)