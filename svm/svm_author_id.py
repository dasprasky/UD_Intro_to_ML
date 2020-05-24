#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import  svm


# ### features_train and features_test are the features for the training
# ### and testing datasets, respectively
# ### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
## features_train = features_train[:len(features_train)/100]        #size decrease - 1%
## labels_train = labels_train[:len(labels_train)/100]              #size decrease - 1% of dataset

# ### your code goes here ###
clf=svm.SVC(kernel='rbf', C=10000)
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
pred=clf.predict(features_test)
t1 = time()
acc=clf.score(features_test, labels_test)
print "test time:", round(time()-t1, 3), "s"


print 'The accuracy of SVM classifier is : ', acc
list=[10,26,50]
for n in list:
    print 'The', n,'th element is : ', pred[n]

num_chris=0
for i in pred:
    if i==1:
        num_chris+=1
print 'Number of data in Chris\'s class ', num_chris