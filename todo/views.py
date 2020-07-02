from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")
        #data = pd.read_csv('User.xls')
        #self.write(data)

class ProfileHandler(RequestHandler):
    """Print database as the response body."""

    def initialize(self, database):
        self.database = database
        self.write(dict(database=database))

    #def get(self, userid):
        #self.userid = userid



