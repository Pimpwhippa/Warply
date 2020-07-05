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

userdata = pd.read_csv('User_s.xls', sep='\', header =0)

class FileHandler(RequestHandler):

    def get(self):
        userdata.to_json(self)
        self.write("ajaja")

#class StaticHandler(StaticFileHandler):
    #def initialize(self, myfile):
        #self.myfile = myfile
        #print("ruleaw")

#how to know if initialize() get called or not?

    #def get(self, name):
        #self.write(myfile.read())




