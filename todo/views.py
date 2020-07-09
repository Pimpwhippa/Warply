from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os
import json
import pandas as pd
import csv

class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):
    def get(self, MainHandler):
        #items = ["Baba", "Item 2", "Item 3"]
        #with open('arai.csv') as f:
        var1 = "key"
        var2 = "value"
        csv_dic={var1:[], var2:[]}
        csvFile = csv.reader(open('/home/pimpwhippa/Works/tornado_todo/todo/arai.csv'))
        for row in csvFile:
            csv_dic[var1].append(row[0])
            csv_dic[var2].append(row[1])
        self.write(csv_dic)