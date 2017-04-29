import time
import json
import random
import urllib2
from bottle import *
import cPickle as pkl

AAs=None #Algorethmes acuracy score
WAS=None #waether acuracy score
pers=(AAs+WAS)/2
clf,regg=pkl.load(open('trained.pkl','rb'))


def p(array): return array.values() #convert a dict to array
'func not Along With Api/Data, FIX'

def predict(fnum):
    f=getweather(fnum)
    clf_val=clf.predict(f)
    if clf_val==1:
       return [1,regg.predict(f)]
    return clf_val
    
def tpl(key,**args):
    html=pkl.load('html.pkl')
    return html[key].format(**args)
    
def getweather(fnum):
    #day=day of departure
    #day2=day of arival
    #airport1=[longatide,lateatide](same for a2)
    a1,a2,day,day2=getflight(fnum)
    A1W=json.loads(urllib2.urlopen('\
         https://api.openweathermap.org/data/2.5/forecast/ \
         daily?lat={0}&lon={1}&cnt={2}'.format(a1[0],a1[1],day)).read())
    A2W=json.loads(urllib2.urlopen('\
         https://api.openweathermap.org/data/2.5/forecast/ \
         daily?lat={0}&lon={1}&cnt={2}'.format(a2[0],a2[1],day)).read())
    
    return [p(A1W),p(A2W)]
    
def getflight(fnum):
    #flight API
    return (a1,a2,day,day2)


@route('/')
def index():
    return tpl('index')
