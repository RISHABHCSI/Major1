from sklearn import svm
import numpy as np
import generateFeatures
import generateSumm
from sklearn import preprocessing

X=[]
outputSummary=[]

for i in generateFeatures.noOfChars:
	X.append([i])
for j in range(0,len(generateFeatures.punctuation)):
	X[j].append(generateFeatures.punctuation[j])
for j in range(0,len(generateFeatures.totalWords)):
	X[j].append(generateFeatures.totalWords[j])	
for j in range(0,len(generateFeatures.distinctWords)):
	X[j].append(generateFeatures.distinctWords[j])	
for j in range(0,len(generateFeatures.StopWords)):
	X[j].append(generateFeatures.StopWords[j])	
for j in range(0,len(generateFeatures.sentPos)):
	X[j].append(generateFeatures.sentPos[j])
for j in range(0,len(generateFeatures.stoc)):
	X[j].append(generateFeatures.stoc[j])		
	
# print X	
y=generateFeatures.isPresent
# print len(y),len(X)
clf = svm.SVC()
clf.fit(X, y)  
svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

k=0
for i in X:
	i=np.array(i).reshape(1,-1)
	if clf.predict(i)==1:
		outputSummary.append(generateSumm.Training[k])
	# 	print generateSumm.Training[k]
	print clf.predict(i)	  
	k+=1

f=open('manualSummary','w')
for i in range(0,len(generateSumm.resultList)):
	f.write(str(generateSumm.resultList[i])+'\n')
f.close()

f=open('automatedSummary','w')
for i in range(0,len(outputSummary)):
	f.write(str(outputSummary[i])+'\n')
f.close()		
		