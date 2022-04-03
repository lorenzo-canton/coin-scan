from ast import parse
from http.server import BaseHTTPRequestHandler
import urllib.parse

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(url.query)

        if url.path == '/':
            path = '/index.html'

        if url.path == '/options':
            path = '/index.html'
            params['ema_long'] = int(params['ema_long'][0])
            print(params)

        try:
            page = open(path[1:]).read()
            self.send_response(200)
        except:
            page = '404 not found'
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(page, 'utf-8'))