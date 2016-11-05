import math
import string
from nltk.stem.porter import *
from nltk.corpus import stopwords
import operator
INFINITY = 1000000000

input="Loving you soooooo much GaGa!!"

def removePunc(input):
	exclude = set(string.punctuation) 
	input= ''.join(ch for ch in input if ch not in exclude)
	return input

def convertToLower(inputi):
	return inputi.lower()

def removeRedundant(input):
	count=1
	temp=""
	temp+=input[0]
	for i in range(1,len(input)):
		if(input[i]!=input[i-1]):
			if(count<=3):
				for k in range(1,count):
					temp+=input[i-1]
			temp+=input[i]
			count=1
		else:
			count+=1
	if(count<=3):
		for k in range(1,count):
			temp+=input[i-1]		
	input=temp
	return input

def doStemming(input):
	input=input.decode('utf-8')
	stemmer=PorterStemmer()
	temp=[]
	inputlist=input.split(' ')
	input=""
	for i in range(0,len(inputlist)):
		temp.append(stemmer.stem(inputlist[i]))
	for i in range(0,len(temp)):
		input+=temp[i]+" "
	input=input.rstrip()	
	return input

def generateNGrams(input_list,n):
	return zip(*[input_list[i:] for i in range(n)])

def removeStopGrams(grams):
	tempgrams=[]
	for gram in grams:
		tempgram=[]
		for tup in gram:
			for i in range(0,len(tup)):
				if(tup[i] not in (stopwords.words('english'))):
					tempgram.append(tup)
					break
		tempgrams.append(tempgram)
	grams=tempgrams
	return grams

def removeStopWords(comment):
	newComment=""
	comment=comment.split()
	for com in comment:
		if(com not in (stopwords.words('english'))):
			newComment+=com+" "
	newComment=newComment.rstrip()				
	return newComment

def generateDistinct(commentstemp):
	distinct=[]
	for i in range(0,len(commentstemp)):
		for inp in commentstemp[i]:
			if(inp not in distinct):
				distinct.append(inp)
	return distinct	

def similarity(comment1,comment2):
	D=0.0
	for i in range(0,len(comment1)):
		if(comment1[i]==1):
			D+=1.0	
		else:
			if(comment2[i]==1):
				D+=1.0	
	sumi=0
	for i in range(0,len(comment1)):
		sumi+=comment1[i]*comment2[i]
	if(sumi>=D):
		return 1
	else:
		return (sumi*1.0)/D

def distanceBwComments(comment1,comment2):
	k=similarity(comment1,comment2)
	if(k==0):
		return INFINITY
	else:
		return (1.0/k)-1

def centerOfCluster(commentsbelong):
	clusterCoordinate=[]
	for i in range(0,len(commentsbelong[0])):
		sumi=0
		for k in range(0,len(commentsbelong)):
			sumi+=commentsbelong[k][i]
		clusterCoordinate.append(sumi)
	return clusterCoordinate

def auxiliary(comment,cluster):
	sumi=0.0
	if len(comment)==len(cluster):
		for i in range(0,len(comment)):
			if(comment[i]*cluster[i]>2):
				sumi+=2
			else:	
				sumi+=comment[i]*cluster[i]
	return sumi		

def similarityCommentCluster(comment,cluster):
	T=0.0
	for i in range(0,len(comment)):
		if(comment[i]>0):
			T+=2.0
		else:
			if(cluster[i]>0):
				T+=2.0	
	k=auxiliary(comment,cluster)
	if(k<T):
		return (k*1.0)/T
	else:
		return 1	

def distanceCommentCluster(comment,cluster):
	T=0.0
	for i in range(0,len(comment)):
		if(comment[i]>0):
			T+=2.0
		else:
			if(cluster[i]>0):
				T+=2.0
	k=similarityCommentCluster(comment,cluster)
	if(k==0):
		return INFINITY
	else:
		return (1.0/similarityCommentCluster(comment,cluster))-1

def distanceBwClusters(cluster1,cluster2):
	D=0.0
	for i in range(0,len(cluster1)):
		D+=max(cluster1[i],cluster2[i])	
	sumi=0
	for i in range(0,len(cluster1)):
		sumi+=min(cluster1[i],cluster2[i]);
	k=0.0	
	if(sumi>=D):
		k=1
	else:
		k=(sumi*1.0)/D
	if(k==0):
		return INFINITY
	else:
		return (1.0/k)-1	

def radiusOfCluster(cluster,commentsbelong):
	maxi=0.0
	for i in range(0,len(commentsbelong)):
		if len(cluster):
			sumi=distanceCommentCluster(commentsbelong[i],cluster)
			if(sumi>maxi):
				maxi=sumi
	return maxi	

def generateTermVector(commentstemp, distinct):
	termvector=[]
	for comment in commentstemp:
		term=[]
		for dis in distinct:
			if(dis in comment):
				term.append(1)
			else:
				term.append(0)	
		termvector.append(term)
	return termvector	

def generateComments():
	comments=[]
	with open("data2.txt") as f:
		for line in f:
			comments.append(line)
	return comments

def move(clusterBelong):
	centroidPos=[]
	for i in range(0,len(clusterBelong[0])):
		value=0.0
		for j in range(0,len(clusterBelong)):
			value+=clusterBelong[j][i]
		centroidPos.append(value)	
	return centroidPos

def merge(clusternum1,clusternum2,clusters,clustersAssigned):
	for i in range(0,len(clusters[clusternum1])):
		clusters[clusternum1][i]=clusters[clusternum1][i] + clusters[clusternum2][i]
	for i in range(0,len(clustersAssigned)):
		if(clustersAssigned[i]==clusternum2):
			clustersAssigned[i]=clusternum1	
	return clusters,clustersAssigned
	
def classify(comments,clusters,comment,clustersAssigned,k):
	found=0
	maxi=INFINITY
	for i in range (0,len(clusters)):
		if len(clusters[i]):
			if(distanceCommentCluster(comment,clusters[i])!=INFINITY):
				if(distanceCommentCluster(comment,clusters[i])<maxi):
					clustersAssigned[k]=i
					maxi=distanceCommentCluster(comment,clusters[i])
					found=1
	if(found==1):
		clusterBelong=[]
		val=clustersAssigned[k]
		for j in range(0,len(comments)):
			if(clustersAssigned[j]==val):
				clusterBelong.append(comments[j])
		clusters[clustersAssigned[k]]=move(clusterBelong)		
	if(found==0):
		cluster=comment
		clusters.append(cluster)
		clustersAssigned[k]=len(clusters)-1
		
	return clustersAssigned,clusters	

def doBatchSTS(comments,threshold):
	clusters=[]
	# print comments
	clustersAssigned=[-1]*len(comments)
	for k in range(0,len(comments)):
		clustersAssigned,clusters=classify(comments,clusters,comments[k],clustersAssigned,k)	
	nonSinglePointClusters=[]		
	for i in range(0,len(clusters)):
		count=0
		for k in range(0,len(clustersAssigned)):
			if(clustersAssigned[k]==i):
				count+=1
		if(count>1):
			nonSinglePointClusters.append(i)
	
	for i in range(0,len(nonSinglePointClusters)):
		for k in range(0,len(nonSinglePointClusters)):
			if(i!=k):
				if(distanceBwClusters(clusters[nonSinglePointClusters[i]],clusters[nonSinglePointClusters[k]])!=INFINITY):
					clusters,clustersAssigned=merge(nonSinglePointClusters[i],nonSinglePointClusters[k],clusters,clustersAssigned)
	
	nonSinglePointClusters=[]		
	for i in range(0,len(clusters)):
		count=0
		for k in range(0,len(clustersAssigned)):
			if(clustersAssigned[k]==i):
				count+=1
		if(count>1):
			nonSinglePointClusters.append(i)
	
	emptypool=[]
	for i in range(0,len(nonSinglePointClusters)):
		commentsbelongtemp=[]
		commentsbelongIndex=[]
		for j in range(0,len(comments)):
			if(clustersAssigned[j]==nonSinglePointClusters[i]):
				commentsbelongtemp.append(comments[j])
				commentsbelongIndex.append(j)
		while(radiusOfCluster(clusters[nonSinglePointClusters[i]],commentsbelongtemp)>=threshold):
			val=0
			for k in range(0,len(commentsbelongtemp)):
				if(distanceCommentCluster(commentsbelongtemp[val],clusters[nonSinglePointClusters[i]])>=threshold):
					clustersAssigned[commentsbelongIndex[val]]=-1
					temp1=commentsbelongtemp[val]
					temp2=commentsbelongIndex[val]
					del commentsbelongtemp[val:val+1]
					del commentsbelongIndex[val:val+1]
					clustersAssigned,clusters=classify(comments,clusters,temp1,clustersAssigned,temp2)
				else:
					val+=1
	
	return clusters,clustersAssigned

# input=removePunc(input)
# input=convertToLower(input)
# input=removeRedundant(input)
# input=doStemming(input)
# grams=[]
# for i in range(1,4):
# 	grams.append(generateNGrams(input.split(' '),i))	

# print grams
# print "\n\n"
# grams=removeStopGrams(grams)
# print grams

# input1=input
# input2="He is very Intelligent. He is fan of Gaga"
# input3="Richard of Pied Piper is the CEO"

comments=generateComments()
originalComments=tuple(comments)

for i in range(0,len(comments)):
	comments[i]=removePunc(comments[i])
	comments[i]=removeStopWords(comments[i])
	comments[i]=convertToLower(comments[i])
	comments[i]=removeRedundant(comments[i])
	comments[i]=doStemming(comments[i])

commentstemp=[]
for i in range(0,len(comments)):
	commentstemp.append(comments[i].split(' '))

distinct=generateDistinct(commentstemp)	
threshold=6
termvector=[]
termvector=generateTermVector(commentstemp,distinct)


clusters,clustersAssigned=doBatchSTS(termvector,threshold)
# print clusters
# print clustersAssigned
# print "\n\n"
finalcommentsBelong=[]
for i in range(0,len(clusters)):
	commentsbelong=[]
	for j in range(0,len(comments)):
		if clustersAssigned[j]==i:
			commentsbelong.append(j)
	finalcommentsBelong.append(commentsbelong)

# for i in range(0,len(finalcommentsBelong)):
# 	for j in range(0,len(finalcommentsBelong[i])):
# 		print originalComments[finalcommentsBelong[i][j]]
# 	print "\n\n\n\n\n\n"

def generateReqGrams(comm,n):
	gram=[]
	for i in range(0,len(comm)-n+1):
		temp=comm[i:i+n]
		tempstr=""
		for t in temp:
			tempstr+=t+" "
		tempstr=tempstr.rstrip()
		found=0
		for gr in gram:
			if gr[0]==tempstr:
				gr[1]+=1
				found=1
				break
		if found==0:
			gram.append([tempstr,1])		 	
	return gram

def intersect(str1,str2,overlapPercent):
	str1=str1.split()
	str2=str2.split()
	count=0.0
	for word in str2:
		if word in str1:
			count+=1.0
	return count/len(str1)		

def keyCloud(cluster,comments,commentsbelong,overlapPercent,k):
	grams=[]
	comm=[]
	
	for i in range(0,len(commentsbelong)):
		keywords=comments[commentsbelong[i]].split()
		for keyword in keywords:
			comm.append(keyword)		
	for i in range(1,len(comm)+1):
		grams.append(generateReqGrams(comm,i))
	for gram in grams:
		val=0
		for i in range(0,len(gram)):
			if (gram[val][1])<k:
				print gram[val]
				del gram[val]
			else:
				val+=1	
	
	for gram in grams:
		removelist=[]
		for i in range(0,len(gram)):
			for j in range(0,len(gram)):
				if (i!=j and gram[j][1]>gram[i][1]):
					if intersect(gram[j][0],gram[i][0],overlapPercent)>=overlapPercent:
						removelist.append(i)
		gramtemp=[]
		for i in range(0,len(gram)):
			if i not in removelist:
				gramtemp.append(gram[i])
		gram=gramtemp
	

	for i in range(0,len(grams)-1):
		removelist=[]
		for j in range(0,len(grams[i])):
			for m in range(i+1,len(grams)):
				for n in range(0,len(grams[m])):
					if intersect(grams[m][n][0],grams[i][j][0],overlapPercent)>=overlapPercent:
						removelist.append(j)
		gramtemp=[]
		for j in range(0,len(grams[i])):
			if j not in removelist:
				gramtemp.append(grams[i][j])
		grams[i]=gramtemp
	return grams	

def countCommon(comment,grams):
	comment=comment.split()
	count=0
	for word in comment:
		for gram in grams:
			for gr in gram:
				if word in gr[0].split():
					count+=1
	return count				

def visualize(clusters,clustersAssigned,comments,overlapPercent,k):
	output=[]
	for i in range(0,len(clusters)):
		commentsbelong=[]
		for j in range(0,len(clustersAssigned)):
			if clustersAssigned[j]==i:
				commentsbelong.append(j)
		grams=keyCloud(clusters[i],comments,commentsbelong,overlapPercent,k)
		sentenceval={}
		for i in range(0,len(commentsbelong)):
			common=countCommon(comments[commentsbelong[i]],grams)
			if commentsbelong[i] not in sentenceval:
				sentenceval[commentsbelong[i]]=common
		print sentenceval	
		sorted_sentenceval=sorted(sentenceval.items(), key=operator.itemgetter(1))
		retreive=min(3,len(sorted_sentenceval))
		sorted_sentenceval=sorted_sentenceval[len(sorted_sentenceval)-retreive:]
		print sorted_sentenceval
		print grams
		for j in range(0,len(sorted_sentenceval)):
			print comments[sorted_sentenceval[j][0]]
		print "\n\n"	

overlapPercent=0.8
k=1
visualize(clusters,clustersAssigned,originalComments,overlapPercent,k)


