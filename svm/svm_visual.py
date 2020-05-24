
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import  svm
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData


#
# ### features_train and features_test are the features for the training
# ### and testing datasets, respectively
# ### labels_train and labels_test are the corresponding item labels
#features_train, features_test, labels_train, labels_test = preprocess()
#
# #########################################################
# ### your code goes here ###
features_train, labels_train, features_test, labels_test = makeTerrainData()
clf=svm.SVC(kernel='rbf', C=1000.0)
clf.fit(features_train,labels_train)
# clf.predict(features_test)
#########################################################

import numpy as np
import pylab as pl

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]



### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
