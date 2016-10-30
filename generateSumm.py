import os
import summarize
sentPos=[]
# location of directory you want to scan
loc = '/Major1 Project/nlp/Datasets/Timeline17/Data/H1N1_guardian/InputDocs'
# global dictonary element used to store all results
global k1 
k1 = {}

Summary=[]
Training=[]
resultList=[]    

# scan function recursively scans through all the diretories in loc and return a dictonary
def scan(element,loc):

    le = len(element)

    for i in range(le):   
        try:

            second_list = os.listdir(loc+'/'+element[i])
            temp = loc+'/'+element[i]
            print "....."
            # print "Directory %s " %(temp)
            print " "
            # print second_list
            k1[temp] = second_list
            scan(second_list,temp)

        except OSError:
            pass

    return k1 # return the dictonary element    


# initial steps
# try:
def generateSum():
    initial_list = os.listdir(loc)
    # print initial_list

    for i in range(0,len(initial_list)):
        # print initial_list[i]
        sec=os.listdir(loc+'/'+initial_list[i])
        for j in sec:
            k=0
            ob=open(loc+'/'+initial_list[i]+'/'+j)
            Summary.append(summarize.generateSum(loc+'/'+initial_list[i]+'/'+j))
            a=ob.readlines()
            s=""
            for l in a:
                Training.append(l)
                sentPos.append(k)
                k+=1
         
    for s in Summary:
        for i in s:
            resultList.append(i)
generateSum()
