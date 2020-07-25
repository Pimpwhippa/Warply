from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import functools
from tornado import gen
from datetime import datetime
import pandas as pd
import json


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):

    #@functools.lru_cache(maxsize=500)
    @gen.coroutine
    def get(self, MainHandler):

        csvFile = pd.read_csv('/home/pimpwhippa/Works/tornado_todo/todo/User_s_no_binary.csv', parse_dates = ['last_login'])
        now = datetime.now()
        csvFile['now'] = now
        csvFile['since'] = csvFile['now'] - csvFile['last_login']    
        #csvFile = csvFile.to_dict()
        many = len(csvFile['since'])
        self.write(chr(many))
        #self.write(new_dict[v])
        #self.write(new_dict[v])
        #KeyError: '2020-05-02 21:11:11'