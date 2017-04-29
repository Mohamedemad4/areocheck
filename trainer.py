#!/usr/bin/python2
import cPickle as pkl
from sklearn.svm import SVC,SVR
from sklearn.metrics import accuracy_score


f_train,l_train,f_test,l_test=pkl.load(open('pkls/regg_data.pkl','rb'))

f1_train,l1_train,f1_test,l1_test=pkl.load(open('pkls/clf_data.pkl','rb'))

regg=SVR()
regg.fit(f_train,l_train)

clf=SVC()
clf.fit(f1_train,l1_train)

print 'Regression Accuracy Score {0}%'.format(accuracy_score(l_test,regg.predict(f_test))*100)
print 'Classifier Accuracy Score {0}%'.format(accuracy_score(l1_test,clf.predict(f1_test))*100)

print "dumping trained classes"
pkl.dump((clf,regg),open('trained.pkl','wb'))
print '#'*596
print "DONE ,Good Luck"
