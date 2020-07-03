from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os
import json


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class IndexHandler(RequestHandler):
    def get(self, arg):
        self.render('User_s.xls')

class StaticHandler(StaticFileHandler):
    def initialize(self, myfile):
        self.myfile = myfile

    def get(self, name):
        self.write(myfile.read())

#class FileItem:
    #def __init__(self, fname):
        #self.fname = fname
        #json.dumps(myfile)


