#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.tree import DecisionTreeClassifier as DTC

clf40 = DTC(min_samples_split=40)

print "Features:", len(features_test[0])

t0 = time()
clf40.fit(features_train, labels_train)
print "Fitting:", time() - t0

t0 = time()
pred40 = clf40.predict(features_test)
print "Predicting:", time() - t0

print "Score:", clf40.score(features_test, labels_test)

#########################################################


