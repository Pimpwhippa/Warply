# __init__.py
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from tornado.web import StaticFileHandler
from todo.views import HelloWorld
from todo.views import MainHandler
from todo.views import Render
#from todo.views import OutputHandler

import os

define('port', default=8888, help='port to listen on')

def main():
    """Construct and serve the tornado application."""

    app = Application([
        ('/', HelloWorld),
        ('/item/(.*)', MainHandler),
        ('/render/(.*)', Render),
        #('/output/(.*)', OutputHandler)
        #('/lastlogin/(.*)', LastLogin, {"last_login": self.MainHandler}),
        ('/data/(.*)', StaticFileHandler, {'path': '/home/pimpwhippa/Works/tornado_todo/todo'}),
        #('/data', DataLoader)
        #static_path=os.path.join(SRC, "static")
        ])
        
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
