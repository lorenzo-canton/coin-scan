# API timeframes to minute
timeframe = {
    'm1': 1,
    'm5': 5,
    'm15': 15,
    'h1': 60,
    'h2': 2 * 60,
    'h3': 3 * 60,
    'h4': 4 * 60,
    'h6': 6 * 60,
    'h8': 8 * 60,
    'D1': 24 * 60,
    'W1': 7 * 24 * 60,
    'M1': 30 * 24 * 60
}
# Api token
TOKEN = '546a088987e0e775aa7834095f187d3b1c4e4e06'

pip_cost = .0911
lot_size = 10

trader = [
    {
        "symbol": 'GBP/JPY',
        "timeframe": 'm1',
        "ema_fast": 8,
        "ema_slow": 20
    }
]
