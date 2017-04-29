import sqlite3
import gzip
import pandas as pd
import cPickle as pkl
conn = sqlite3.connect('dbb.db')
cur=conn.cursor()

for i in open('2016.csv','r'):
    i=i.split(',')
    #fix
    cur.execute('insert weather,froma,date into weather_table values({0},{1},{2})'.format([i[0],i[1]] ,i[2],i[3],i[4]))
    conn.commit()
