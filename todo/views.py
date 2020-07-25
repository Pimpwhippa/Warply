from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import functools
from tornado import gen
from datetime import datetime
import pandas as pd
import json
from datetime import timedelta


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):

    #@functools.lru_cache(maxsize=500)
    @gen.coroutine
    def get(self, MainHandler):

        csvFile = pd.read_csv('/home/pimpwhippa/Works/tornado_todo/todo/later_user.csv', parse_dates = ['last_login'])
        now = datetime.now()
        csvFile['now'] = now
        csvFile['since'] = csvFile['now'] - csvFile['last_login']
        csvFile['havent_login_for_a_week'] = csvFile['since'] > timedelta(days=7)
        nono = sum(csvFile['havent_login_for_a_week'] == True)
        num_hvnt_login_for_a_week = str(nono).encode("utf-8").decode("utf-8")
        #self.write(bytes([nono])) ValueError: bytes must be in range(0, 256)
        
        self.write(num_hvnt_login_for_a_week)
