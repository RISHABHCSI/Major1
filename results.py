import generateSumm
import classify

manualSummary=generateSumm.resultList
automatedSummary=classify.outputSummary

intersection=0.0
for i in range(0,len(automatedSummary)):
	for j in range(0,len(manualSummary)):
		if(str(automatedSummary[i]).strip()==str(manualSummary[j]).strip()):
			intersection+=1.0
			break
print intersection
print len(automatedSummary)
print len(manualSummary)

precision=intersection/len(automatedSummary)
print precision
recall=intersection/len(manualSummary)
print recall			
