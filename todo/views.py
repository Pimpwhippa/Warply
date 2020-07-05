from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os
import json
import pandas as pd

class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)

class DataLoader(RequestHandler):

    def lots_of_data_func():
        df = pd.read_csv('User_s.xls', header = 0, sep=" ")
        return df

    async def get(self):
       data = await lots_of_data_func()
       self.write({"data":data})

def routes():
    return Application([
        (r"/", MainHandler),
    ])

#userdata = pd.read_csv('User_s.xls', sep='\', header =0)

#class FileHandler(RequestHandler):

    #def get(self):
        #userdata.to_json(self)
        #self.write("ajaja")

#class StaticHandler(StaticFileHandler):
    #def initialize(self, myfile):
        #self.myfile = myfile
        #print("ruleaw")

#how to know if initialize() get called or not?

    #def get(self, name):
        #self.write(myfile.read())




