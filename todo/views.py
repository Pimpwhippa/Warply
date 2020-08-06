from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import functools
from tornado import gen
from datetime import datetime
import pandas as pd
import json
from datetime import timedelta
from pyroaring import BitMap
import random


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")

class MainHandler(RequestHandler):

    #@functools.lru_cache(maxsize=500)
    @gen.coroutine
    def get(self, MainHandler):

        csvFile = pd.read_csv('/home/pimpwhippa/Works/tornado_todo/todo/later_user.csv', parse_dates = ['last_login'])
        now = datetime.now()
        csvFile['now'] = now
        csvFile['since'] = csvFile['now'] - csvFile['last_login']
        csvFile['havent_login_for_a_week'] = csvFile['since'] > timedelta(days=7)
        nono = sum(csvFile['havent_login_for_a_week'] == True)
        num_hvnt_login_for_a_week = str(nono).encode("utf-8").decode("utf-8")
        
        self.write(num_hvnt_login_for_a_week)

class UserTag(RequestHandler):
    def get(self, UserTag):

        customer = pd.read_csv('/home/pimpwhippa/Works/tornado_todo/todo/binary_tag.csv')
        tag = customer['tag'].to_dict()   
#gen 500 randint
        ks = []
        for _ in range(500):
            n = random.randint(0,10)
            ks.append(n)

#gen 500 rows of BitMap set
#by taking those 500 randint as k for random.sample(range(1, 11), 3) <--k =3
        rows = []
        for k in ks:
            row = BitMap(random.sample(range(1,11), k))
            rows.append(row)

#make a DataFrame of 500 row from dict of BitMap sets
        df = pd.DataFrame(data=rows, columns= ['tag1','tag2', 'tag3', 'tag4','tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10'])

#find no. of rows that have [1,2] in it
        Q1 = df.loc[(df['tag1'] == 1.0) & (df['tag2'] == 2.0)]
        num_user_with_tag1_and_tag2 = str(len(Q1)).encode("utf-8").decode("utf-8")
        self.write(num_user_with_tag1_and_tag2)

#find row index of all rows that have [1]
        df['id'] = range(1,501)
        IDtag1 = df.loc[df['tag1'] == 1.0]['id']
        self.write(IDtag1.to_dict())


