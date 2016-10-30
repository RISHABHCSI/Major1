import generateSumm
import summarize
import math
from nltk.corpus import stopwords

totalWords=[]
distinctWords=[]
noOfChars=[]
StopWords=[]
punctuation=[]
sentPos=[]	
stos=[]
stoc=[]
isPresent=[]
words=[]
sentencesvector=[]
# def totalWords():
# def distinctWords():
def noOfCharsPuncTotalWordsDistinctWords():
	for i in generateSumm.Training:
		temp=i.split()
		count=0
		punc=0
		words=0
		distinctwords=0
		distinct=[]
		for t in temp:
			if t not in distinct:
				distinct.append(t)
			words+=1
			for c in t:
				count+=1
				if (ord(c)>122 or ord(c)<97) and (ord(c)>90 or ord(c)<65):
					punc+=1 
		chars=count-punc
		totalWords.append(words-punc)
		punctuation.append(punc)
		noOfChars.append(chars)
		for i in distinct:
			if len(i)==1 and ((ord(c)>122 or ord(c)<97) and (ord(c)>90 or ord(c)<65)):
				distinct.remove(i)
		distinctWords.append(len(distinct))

def countStopWords():
	for i in generateSumm.Training:
		temp=i.split()
		count=0
		for t in temp:
			if(t not in (stopwords.words('english'))):
				count+=1
		StopWords.append(len(temp)-count)

def sentencePos():
	sentPos=generateSumm.sentPos

def isPunc(ch):
	if len(ch)==1 and ((ord(ch)>122 or ord(ch)<97) and (ord(ch)>90 or ord(ch)<65)):
		return 1
	return 0	

def stossimilar():
	ones=[]
	for i in generateSumm.Training:
		temp=i.split()
		for t in temp:
			if t not in words and (isPunc(t)==0):
				words.append(t)		
		for i in range(0,len(generateSumm.Training)):
			sentencesvector.append([])
			stos.append(0.0)
			ones.append(0)
	
	for i in range(0,len(words)):
		for j in range(0,len(generateSumm.Training)):
			if words[i] not in generateSumm.Training[j]:
				sentencesvector[j].append(0)
			else:
				sentencesvector[j].append(1)
				ones[j]+=1				

	# for i in range(0,len(generateSumm.Training)):
	# 	print i
	# 	print "\n"
	# 	for j in range(0,len(generateSumm.Training)):
	# 		print j
	# 		similar=0.0
	# 		if i!=j:
	# 			for k in range(0,len(words)):
	# 				if(sentencesvector[i][k]==1 and sentencesvector[j][k]==1):
	# 					similar+=1.0
	# 		stos[i]+=similar/(ones[i]*ones[j])
	# print stos[0],stos[1]		
	# maxi=0.0
	# for i in range(0,len(stos)):
	# 	if stos[i]>maxi:	
	# 		maxi=stos[i]
	# for i in range(0,len(stos)):
	# 	if stos[i]!=0:
	# 		stos[i]=stos[i]/maxi					
	# print stos[0],stos[1]

def diff(sentence,centroid):
	diff=0.0
	for i in range(0,len(sentence)):
		diff+=(sentence[i]-centroid[i])*(sentence[i]-centroid[i])
	diff=math.sqrt(diff)
	return diff

def stocentroidsimilar():	
	centroid=[]
	for i in range(0,len(words)):
		centroid.append(0.0)
	for i in range(0,len(generateSumm.Training)):
		for j in range(0,len(words)):
			if sentencesvector[i][j]==1:
				centroid[j]+=1.0
	for i in range(0,len(centroid)):
		centroid[i]=centroid[i]/len(generateSumm.Training)
	for i in range(0,len(generateSumm.Training)):
		stoc.append(diff(sentencesvector[i],centroid))	
	maxi=0.0
	for i in range(0,len(stoc)):
		if stoc[i]>maxi:
			maxi=stoc[i]
	for i in range(0,len(stoc)):
		if stoc[i]!=0.0:
			stoc[i]=stoc[i]/maxi
	

def generatelabel():
	n=0
	# print str(generateSumm.Training[0]).strip()==str(generateSumm.resultList[0]).strip() 

	# return
	for i in generateSumm.Training:
		# print generateSumm.resultList[0]
		# return
		booli=False
		for j in generateSumm.resultList:
			if(str(i).strip()==str(j).strip()):
				booli=True
				break
		if booli:
			isPresent.append(1)
		else:
			isPresent.append(0)		

	
noOfCharsPuncTotalWordsDistinctWords()
countStopWords()
generatelabel()
sentencePos()
stossimilar()
stocentroidsimilar()

