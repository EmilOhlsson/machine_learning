#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
### it's all yours from here forward!  
features_train, features_test, labels_train, labels_test = \
    train_test_split(features,labels, random_state=42, test_size=.3)
clf = DTC()
clf.fit(features_train, labels_train)

predictions = clf.predict(features_test)
score = clf.score(features_test, labels_test)
print "Accuracy:", score
print sum(predictions), "predicted in the test set"

print confusion_matrix(labels_test, predictions)
print "precision", precision_score(labels_test, predictions)
print "recall", recall_score(labels_test, predictions)

preds = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
actuals = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print confusion_matrix(actuals, preds)
print "precision:", precision_score(actuals, preds)
print "recall:", recall_score(actuals, preds)