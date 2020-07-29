from pyroaring import BitMap
import random
import pandas as pd

#gen 500 randint
ks = []
for _ in range(500):
    n = random.randint(0,10)
    ks.append(n)
#print(ks)

#gen 500 rows of BitMap set
#by taking those 500 randint as k for random.sample(range(1, 11), 3) <--k =3
rows = []
for k in ks:
    row = BitMap(random.sample(range(1,11), k))
    rows.append(row)
    #print(rows)

#make a DataFrame of 500 row from dict of BitMap sets
df = pd.DataFrame(data=rows, columns= ['tag1','tag2', 'tag3', 'tag4','tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10'])
#print(df)

#find no. of rows that have [1,2] in it
#Q1 = df[row.contains_range(1,3) == True]
Q1 = df.loc[(df['tag1'] == 1.0) & (df['tag2'] == 2.0)]
print(len(Q1))

#find row index of all rows that have [1]
df['id'] = range(1,501)
IDtag1 = df.loc[df['tag1'] == 1.0]['id']
print(IDtag1)
