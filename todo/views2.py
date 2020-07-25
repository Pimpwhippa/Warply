from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import functools
from tornado import gen
import csv
from datetime import datetime
import pandas as pd
import json
from json import dumps


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):

    #@functools.lru_cache(maxsize=500)
    @gen.coroutine
    def get(self, MainHandler):
        #items = ["Baba", "Item 2", "Item 3"]
        #with open('arai.csv') as f:
        
        var1 = "userid"
        var2 = "last_login"
        #csv_dic={var1:[], var2:[]}
        var3 = "since"
        csv_dic={var2:[], var3:[]}
        for item in var3:
            item = datetime.now()

        #now = datetime.now()
        #var3 = datetime.now() #csv_dic[var3]
        #last_login = csv_dic['last_login']
        csvFile = csv.reader(open('/home/pimpwhippa/Works/tornado_todo/todo/User_s_no_binary.csv', encoding ='us-ascii'))
        for row in csvFile:
            #csv_dic[var1].append(row[0])
            csv_dic[var2].append(row[1])
            csv_dic[var3].append(item)
            #csv_dic[var4].append(row[3])
        self.write(csv_dic)
        self.write("more than 7 days")

class Render(RequestHandler):
    def get(self, Render):
        #la = ["wawa", "wowo", "wuwu"]
        var1 = "key"
        var2 = "value"
        #key2 is a better value for var2, it's second coloumn name, coz after this there'll be their values

        csv_dic={var1:[], var2:[]}
        #last_login = csv_dic['last_login']
        csvFile = csv.reader(open('/home/pimpwhippa/Works/tornado_todo/todo/User_s_no_binary.csv', encoding ='us-ascii'))
        #la = open("/home/pimpwhippa/Works/tornado_todo/todo/arai.csv", "r", encoding="utf-8")
        #la = csv.DictReader("/home/pimpwhippa/Works/tornado_todo/todo/arai.csv", "r")

        for row in csvFile:
            csv_dic[var1].append(row[0])
            csv_dic[var2].append(row[1])
        self.render("template.html", title= "render_csv", items=row) #items = row? the best so far?
        #cannot render() after finish() so only get the last row of values??