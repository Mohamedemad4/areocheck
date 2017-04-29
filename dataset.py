#!/usr/bin/python

#########Legend##############
##2 canceled 0 OK 1 Dealyed##
#############################

import os
import sqlite3
import pandas as pd
import cPickle as pkl
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile , f_classif,f_regression

' do sql , do headers weather_data , do city api'  

pkl.HIGHEST_PROTOCAL=3

sr=SelectPercentile(Percentile=50,score_func=f_classif)
sc=SelectPercentile(Percentile=50,score_func=f_regression)

flight_dataframe = pd.read_csv('pkls/flight_data.csv',header=None)
flight_dataset = flight_dataframe.values
flight_label=[]
flight_regg_label=[]
flight_regg_data=[]
cur= #something

for flight in flight_dataset:
    if flight[5]=='CANCELLED':
        flight_label.append(2)
    if flight[6]!='WEATHER_DELAY':
        flight_label.append(0)
    #get irrlevent and set to None
    
    flight=np.delete(flight,[0,1,2])
    
    flight=np.hstack(flight,exec(sq('select weather from weather_table where date={0} and dest={2} and from={1}'.format(flight[0],flight[1],flight[2]))))
    if flight[5]>2:
        flight_label.append(1)
        fligh_regg_label.append(flight[5])
        fligh_regg_data.append(flight)
    
            
#run SelectPercentile
sr.fit(flight_regg_data,flight_regg_label)
flight_regg_data=sr.transform(flight_regg_data)

sc.fit(flight_dataset,flight_label)
flight_regg_data=sc.transform(flight_dataset)


pkl.dump(train_test_split(flight_dataset,flight_label,test_size=0.5),open('clf_data.pkl','wb+'))
pkl.dump(train_test_split(flight_regg_data,flight_regg_label,test_size=0.5),open('regg_data.pkl','wb+'))
