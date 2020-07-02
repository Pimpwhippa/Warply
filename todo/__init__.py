# __init__.py
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from todo.views import HelloWorld
from todo.views import ProfileHandler
import pandas as pd

define('port', default=8888, help='port to listen on')

my_cols = [str(i) for i in range(10000)] # create some row names

#database = pd.read_csv('User_with_binary_tag.xls','rb',
database = pd.read_csv('User_s.xls','rb',
                        names=my_cols,
                        header=None,
                        engine="python")

settings = {
'debug': True,
'autoreload': True,
'static_path': 'Works/tornado_todo/User_s.xls'
}

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/', HelloWorld),
        #('/user_not_login_num', HelloWorld)
        (r'/user/(.*)', ProfileHandler, dict(database=database))
    ], **settings
)

    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
