import generateSumm
import summarize

totalWords=[]
distinctWords=[]
noOfChars=[]
StopWords=[]
punctuation=[]
sentPos=[]
stos=[]
stoc=[]
isPresent=[]
# def totalWords():
# def distinctWords():
def noOfCharsPunc():
	for i in generateSumm.Training:
		temp=i.split()
		count=0
		punc=0
		for t in temp:
			for c in t:
				count+=1
				if (ord(c)>122 or ord(c)<97) and (ord(c)>90 or ord(c)<65):
					punc+=1 
		chars=count-punc
		punctuation.append(punc)
		noOfChars.append(chars)	

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

	
noOfCharsPunc()
generatelabel()

