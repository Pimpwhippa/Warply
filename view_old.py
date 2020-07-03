def analysis(filename):
    x = pd.DataFrame(database)
    return render_template("analysis.html", name=filename, data=x)

application = tornado.web.Application([
(r"/",Handler),
(r"/(programming.gif)", tornado.web.StaticFileHandler, {'path':'./'}) <--Add!
])

class ProfileHandler(RequestHandler):
    #"""Print database as the response body."""

    #def initialize(self, database):
        #self.database = database
        #self.write(dict(database=database))

class MyFileHandler(StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(MyFileHandler, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(MyFileHandler, self).get(self.filename, include_body)
        #self.render('User_s.xls')

#class Handler(RequestHandler):
    #def get(self):

class IndexHandler(RequestHandler):
    def get(self, param):
        print("\n\nthis is a get request from indexhandler:")
        if param:
            #print("frontend/" + param)
            self.render("frontend/" + param)
            print("I'm html")
        else:
            print("index.html")
            self.render("index.html")