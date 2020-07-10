from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import functools
from tornado import gen
import csv
import pandas as pd


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):

    #@functools.lru_cache(maxsize=500)
    #@gen.coroutine
    def get(self, MainHandler):
        #items = ["Baba", "Item 2", "Item 3"]
        #with open('arai.csv') as f:
        
        var1 = "userid"
        var2 = "last_login"
        csv_dic={var1:[], var2:[]}
        csvFile = csv.reader(open('/home/pimpwhippa/Works/tornado_todo/todo/User_s_no_binary.csv', encoding ='us-ascii'))
        for row in csvFile:
            csv_dic[var1].append(row[0])
            csv_dic[var2].append(row[1])
            #csv_dic[var3].append(row[2])
            #csv_dic[var4].append(row[3])
        self.write(csv_dic)
        #return csv_dic

    #def get(self, last_login):
        #self.write(csv_dic[var2])