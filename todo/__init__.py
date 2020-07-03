# __init__.py
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from todo.views import HelloWorld
from todo.views import IndexHandler
from todo.views import StaticHandler
import os

import pandas as pd
my_cols = [str(i) for i in range(10000)] # create some row names

define('port', default=8888, help='port to listen on')
#myfile = open('User_s.xls', 'rb')
myfile = pd.read_csv('User_s.xls', sep='|', names=my_cols , encoding='latin-1')

def main():
    """Construct and serve the tornado application."""

    settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "tornado_todo")
        }
    app = Application([
        ('/', HelloWorld),
        (r'/user/(.*)', IndexHandler),
        #(r'/user/User_s.xls', StaticHandler, {'path': './User_s.xls'})
        (r'/user/User_s.xls', StaticHandler, dict(path=settings['static_path']))
        ], **settings)
    
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
