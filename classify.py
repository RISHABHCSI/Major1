from sklearn import svm
import numpy as np
import generateFeatures
from sklearn import preprocessing

X=[]

# print generateFeatures.noOfChars
# print generateFeatures.punctuation
for i in generateFeatures.noOfChars:
	X.append([i])
for j in range(0,len(generateFeatures.punctuation)):
	X[j].append(generateFeatures.punctuation[j])
# print X	
y=generateFeatures.isPresent
# print len(y),len(X)
clf = svm.SVC()
clf.fit(X, y)  
svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
# X= X.reshape(1,-1)
for i in X:
	i=np.array(i).reshape(1,-1)
	print clf.predict(i)