import numpy as np
import pandas as pd
from datetime import datetime, timedelta

name = ['xGfeKtAkii', 'UdwpuCqcyB', 'MsMEoyZtPF', 'IPSIFrBWjs', 'zDGmboSsFG', 
        'DHuidZmCrG', 'idtkBuMcgA', 'dSjeAEPNKH', 'fIWeQmziPE', 'XoyDFtUBxY']

userid = range(1, 11, 1)

list_of_tuples = list(zip(name, userid))

user = pd.DataFrame(list_of_tuples, columns = ['name', 'userid'])

user['tag1'] = [0,1,1,0,0,0,0,1,0,1]
user['tag2'] = [1,1,0,0,0,1,0,0,0,0]
user['tag3'] = [0,0,0,0,0,0,1,1,1,0]
user['tag4'] = [0,0,0,0,1,0,0,1,0,1]
user['tag5'] = [0,0,1,0,0,0,0,0,0,0]
user['tag6'] = [1,0,0,0,0,1,0,0,0,0]
user['tag7'] = [0,1,0,0,0,0,0,0,1,1]
user['tag8'] = [0,0,0,0,0,0,0,1,0,0]
user['tag9'] = [0,0,0,0,0,0,0,0,0,0]
user['tag10'] = [0,0,0,0,0,0,1,0,0,0]

rt = ['2020-05-16 22:23:09',
'2020-04-06 09:02:52',
'2020-06-16 22:52:33',
'2020-02-03 05:29:22',
'2020-03-21 21:43:52',
'2020-01-17 03:14:39',
'2020-02-07 19:26:29',
'2020-06-15 02:50:46',
'2020-04-07 21:01:33',
'2020-06-14 15:58:08']

user['last_login'] = rt
user['now'] = str(datetime.now())

datetimenow = pd.to_datetime(user['now'])
lastlogin = pd.to_datetime(user['last_login'])
since = datetimenow - lastlogin
havent_login_for_a_week = since > timedelta(days=7)

#session management: how many users have not log in for a week?
len(havent_login_for_a_week)

#how many users have tag1 and tag2'
user.loc[(user['tag1'] == 1) & (user['tag2'] == 1)]

#what are the ids of users with tag1
user.loc[user['tag1'] == 1]['userid']

