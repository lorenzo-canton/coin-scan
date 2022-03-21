import logging
import threading
import time


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


def thread_function(name, tf):
    while True:
        logging.info("Thread %s", name)
        time.sleep(timeframe[tf] * 60)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    traders = [
        {
            'target' : thread_function,
            'name' : 'uno',
            'tf' : 'm1' 
        },
        {
            'target' : thread_function,
            'name' : 'cinque',
            'tf' : 'm5'
        }
    ]

    for i in traders:
        x = threading.Thread(target=i['target'], args=(i['name'], i['tf'],))
        x.start()
