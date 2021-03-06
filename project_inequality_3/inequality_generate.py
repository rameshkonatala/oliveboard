import numpy as np
import random,time,os
from itertools import combinations
from itertools import permutations




def mainProgram():
	text=''
	class expression:
		def  __init__(self):
			self.items=''

		def isEmpty(self):
			return self.items == ''

		def addRight(self, item):
			self.items+=item

		def addLeft(self, item):
			self.items=item+self.items
		
		def size(self):
			return len(self.items)

		def nothingToLeft(self,item):
			alist=[]
			for i in range(len(self.items)):
				if self.items[i]==item:
					alist.append(i)
			if 0 in alist:
				return True
			else:
				return False


		def nothingToRight(self,item):
			alist=[]
			for i in range(len(self.items)):
				if self.items[i]==item:
					alist.append(i)
			if len(self.items)-1 in alist:
				return True
			else:
				return False

		def returnExpression(self):
			return self.items

	def shuffle(x):
		    x = list(x)
		    random.shuffle(x)
		    return x

	def opposite(operator):
		if operator == symbolDict['greaterThan']:
			return symbolDict['lessThan']
		elif operator == symbolDict['greaterThanEqualTo']:
			return symbolDict['lessThanEqualTo']
		elif operator == symbolDict['equalTo']:
			return symbolDict['equalTo']
		elif operator == symbolDict['lessThan']:
			return symbolDict['greaterThan']
		elif operator == symbolDict['lessThanEqualTo']:
			return symbolDict['greaterThanEqualTo']

	def expressionOpposite(exp):
		if len(exp)==0:
			return ''
		else:
			expression=''
			i=0
			while i<len(exp)-2:
				expression+=exp[len(exp)-i-1]+opposite(exp[len(exp)-i-2])
				i+=2
			return expression+exp[0]

	def filter_list(L):
	    return [x for x in L if not any(set(x)<=set(y) for y in L if x is not y)]


	def createRelations(text):
		global symbolList,symbolDict
		text+='Consider the following:\n'
		symbolList=list(np.random.choice(['*','@','#','$','%','^','&'],5,replace=False))
		symbolList=shuffle(symbolList)
		#symbolList=['*','@','#','$','%']
		symbolDict={'equalTo':symbolList[0],'greaterThan':symbolList[1],'greaterThanEqualTo':symbolList[2],'lessThan':symbolList[3],'lessThanEqualTo':symbolList[4]}
		symbolDictNotation={'is neither smaller nor greater than':symbolList[0],'is neither smaller nor equal to':symbolList[1],'is not smaller than':symbolList[2],'is neither greater nor equal to':symbolList[3],'is not greater than':symbolList[4]}
		for key in symbolDictNotation.keys():
			text+='\'A{}B\' means \'A {} B\'\n'.format(symbolDictNotation[key],key)
		text+='Now in each of the following questions, assuming the given statements to be true, find which of the two conclusions given below them is/are true. \n'
		return text

	text=createRelations(text)


	def checkValidity(exp):
		resultList=[]
		for i in range(len(finalList)):
			if exp[0] in finalList[i] and exp[2] in finalList[i]:
				
				firstIndex=finalList[i].index(exp[0])
				secondIndex=finalList[i].index(exp[2])
				if firstIndex<secondIndex:
					t= finalList[i][firstIndex:secondIndex+1]
				else:
					t= expressionOpposite(finalList[i][secondIndex:firstIndex+1])
				if t not in resultList and expressionOpposite(t) not in resultList:
					resultList.append(t)
		resultList=''.join(resultList)
		negationDict={'greaterThan':[symbolDict['lessThan'],symbolDict['lessThanEqualTo'],symbolDict['greaterThanEqualTo']],'greaterThanEqualTo':[symbolDict['lessThan'],symbolDict['lessThanEqualTo'],symbolDict['greaterThan']],'lessThan':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThanEqualTo']],'lessThanEqualTo':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThan']],'equalTo':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThanEqualTo'],symbolDict['lessThan']]}
		resultSymbolList=[]
		indexResultList=1
		while indexResultList<len(resultList):
			resultSymbolList.append(resultList[indexResultList])
			indexResultList+=2
		symbolDictReverse=dict((v, k) for k, v in symbolDict.items())
		returnValue=True
		for i in range(len(resultSymbolList)):
			if resultSymbolList[i] in negationDict[symbolDictReverse[exp[1]]]:
				returnValue=False
		if len(resultSymbolList)==0:
			returnValue=False
		return returnValue

	def createExpression():
		digitDict={'alphabets':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		,'numbers':['1','2','3','4','5','6','7','8','9'],'capitals':[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]}
		global q,inputSymbols
		inputSymbols=list(np.random.choice(symbolList,4))
		tempcreateExpression=random.choice([0,2])
		levelType=random.randrange(1,3)
		if tempcreateExpression == 0:
			if levelType==1:
				q=shuffle(digitDict['alphabets'])[:5]
			else:
				q=shuffle(digitDict['alphabets'])[:6]
		elif tempcreateExpression==1:
			if levelType==1:
				q=shuffle(digitDict['numbers'])[:5]
			else:
				q=shuffle(digitDict['numbers'])[:6]
		else:
			if levelType==1:
				q=shuffle(digitDict['capitals'])[:5]
			else:
				q=shuffle(digitDict['capitals'])[:6]
		if levelType==1:
			digitList=[[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[3],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[1],q[3]],[q[1],q[4]]]]
		else:
			digitList=[[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[4],q[5]]],[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[3],q[5]]],[[q[0],q[1]],[q[1],q[2]],[q[3],q[4]],[q[3],q[5]]]]	
		temprandom=random.randrange(0,3)
		
		binaryPair=list(digitList[temprandom])

		if levelType==1:
			if temprandom==0:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1],binaryPair[1][1],binaryPair[2][1],binaryPair[3][1]]]
				
			elif temprandom==1:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1],binaryPair[1][1],binaryPair[2][1]],[binaryPair[3][0],binaryPair[3][1]]]
				
			else:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1],binaryPair[1][1]],[binaryPair[2][1],binaryPair[2][0],binaryPair[3][1]]]
				
		else:
			if temprandom==0:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1]],[binaryPair[1][0],binaryPair[1][1],binaryPair[2][1],binaryPair[3][1]]]
				
			elif temprandom==1:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1]],[binaryPair[1][0],binaryPair[1][1],binaryPair[2][1]],[binaryPair[3][0],binaryPair[3][1]]]
				
			else:
				
				commonSolution=[[binaryPair[0][0],binaryPair[0][1],binaryPair[1][1]],[binaryPair[3][1],binaryPair[2][0],binaryPair[2][1]]]
				
		binaryPair=shuffle(binaryPair)
		inputExpression=''
		for i in range(len(binaryPair)):
			inputExpression+=str(binaryPair[i][0]+inputSymbols[i]+binaryPair[i][1])+str(',')
		
		return inputExpression[:len(inputExpression)-1],commonSolution


	

	def createSolution(question):
		found=False
		for i in range(len(finalList)):
			if question[0] in finalList[i] and question[2] in finalList[i]:
				firstIndex=finalList[i].index(question[0])
				secondIndex=finalList[i].index(question[2])
				if firstIndex>secondIndex:
					return [finalList[i][secondIndex:firstIndex+1]]
				else:
					return [finalList[i][firstIndex:secondIndex+1]]
				found=True
				break
		if not found:
			for i in range(len(finalList)):
				if question[0] in finalList[i]:
					exp1=finalList[i]
					break
			for i in range(len(finalList)):
				if question[2] in finalList[i]:
					exp2=finalList[i]
			return [exp1,exp2]



	def createQuestion(condition):
		global infiniteLoopCount
		infiniteLoopCount=0
		conditionMet=False
		question=''
		while not conditionMet:
			variables=list(np.random.choice(q,2,replace=False))
			symbol=random.choice(inputSymbols)
			question=str(variables[0]+symbol+variables[1])
			conditionMet=(condition==checkValidity(question))
			for i in range(len(symbolList)):
				if str(question[0]+symbolList[i]+question[2]) in expression_list or str(question[2]+symbolList[i]+question[0]) in expression_list :
					conditionMet=False
			if infiniteLoopCount==100:
				break
			infiniteLoopCount+=1

			#print question
		return question


	def main(expression_list):
		def equation(expression_list):
			expression_list=list(expression_list)
			a=expression()
			a.addRight(expression_list.pop(0))
			for i in range(len(expression_list)):
				if expression_list[i][0] in a.returnExpression():
					if a.nothingToRight(expression_list[i][0]):
						a.addRight(expression_list[i][1:])
					elif a.nothingToLeft(expression_list[i][0]):
						expression_list[i]=expression_list[i][:1]+opposite(expression_list[i][1])+expression_list[i][2:]
						a.addLeft(expression_list[i][1:][::-1])
					else:
						pass
				elif expression_list[i][2] in a.returnExpression():
					if a.nothingToRight(expression_list[i][2]):
						expression_list[i]=expression_list[i][:1]+opposite(expression_list[i][1])+expression_list[i][2:]
						a.addRight(expression_list[i][:2][::-1])
					elif a.nothingToLeft(expression_list[i][2]):
						a.addLeft(expression_list[i][:2])
					else:
						pass
			return a.returnExpression()

		expression_list_new=[]
		alist=[]
		for c in permutations(expression_list):
			expression_list_new.append(list(c))

		for i in range(len(expression_list_new)):
			temp=equation(expression_list_new[i])
			if temp not in alist:
				found=False
				for j in range(len(alist)):
					if temp in alist[j] or alist[j] in temp:
						found=True
						break
				if not found:
					alist.append(temp)
		finalList=[]					
		for i in range(len(alist)):
			if expressionOpposite(alist[i]) not in finalList:
				finalList.append(alist[i])
		return finalList

	def createQuestionsList():
		count=0
		questionList=[]
		answerList=[]

		while count<3:


			answerListTemp=random.choice([True,False])
			questionListTemp=createQuestion(answerListTemp)
			if infiniteLoopCount<100:
				toAdd=True
				for i in range(len(inputSymbols)):
					if (str(questionListTemp[0]+inputSymbols[i]+questionListTemp[2]) in questionList) or (str(questionListTemp[2]+inputSymbols[i]+questionListTemp[0]) in questionList):
						toAdd=False
				if toAdd:
					questionList.append(questionListTemp)
					answerList.append(answerListTemp)
					count+=1
		return questionList,answerList


	def convertExp(exp):
		symbolDictActual={'equalTo':'=','greaterThan':'>','greaterThanEqualTo':'>=','lessThan':'<','lessThanEqualTo':'<='}
		actualExp=''
		for i in range(len(exp)):
			if exp[i] in symbolList:
				actualExp+=symbolDictActual[symbolDict.keys()[symbolDict.values().index(exp[i])]]
			else:
				actualExp+=exp[i]
		return actualExp

	def subMain():
		global finalList
		global expression_list
		expression_list,commonSolution=createExpression()
		expression_list=expression_list.split(',')
		finalList= main(expression_list)
		return expression_list,finalList,commonSolution


	finalList_main=[]
	expression_list_main=[]
	i=0
	while i<5:
		expression_list,finalList,commonSolution=subMain()
		questionList,answerList=createQuestionsList()
		correctedExpFinalList=[]
		convertedExp=''
		for item in commonSolution:
			finalExp=''
			for m in range(len(item)-1):
				for symbol in symbolList:
					ans=checkValidity([item[m],symbol,item[m+1]])
					if ans:
						convertedExp=convertExp(''.join([item[m],symbol,item[m+1]]))
						break
				if m==0:
					finalExp+=convertedExp
				else:
					finalExp+=convertedExp[1:]
			correctedExpFinalList.append(finalExp)

		if infiniteLoopCount<100:
			finalList_main.append(finalList)
			expression_list_main.append(expression_list)	
			i+=1
			if answerList[0]==True and answerList[1]==True:
				key=5
			elif answerList[0]==False and answerList[1]==False:
				key=4
			elif answerList[0]==True:
				key=1
			else:
				key=2
			solution1=createSolution(questionList[0])
			solution2=createSolution(questionList[1])
			solution3=createSolution(questionList[2])
			correctedExp1=convertExp(questionList[0])
			
			CommonSolutionText='Common solution is %s\n'%(', '.join(correctedExpFinalList))
			if answerList[0]==True:
				solution1Text='{} means {}\nwhich is True as by decoding the expression we get {} '.format(questionList[0],correctedExp1,convertExp(solution1[0]))
			else:
				if len(solution1)==2:
					solution1Text='{} means {}\nwhich is False as by decoding the expression we get that there is no direct relation between expressions {},{} '.format(questionList[0],correctedExp1,convertExp(solution1[0]),convertExp(solution1[1]))
				else:
					solution1Text='{} means {}\nwhich is False as by decoding the expression we get {} '.format(questionList[0],correctedExp1,convertExp(solution1[0]))	
			correctedExp2=convertExp(questionList[1])
			if answerList[1]==True:
				solution2Text='{} means {}\nwhich is True as by decoding the expression we get {} '.format(questionList[1],correctedExp2,convertExp(solution2[0]))
			else:
				if len(solution2)==2:
					solution2Text='{} means {}\nwhich is False as by decoding the expression we get that there is no direct relation between expressions {},{} '.format(questionList[1],correctedExp2,convertExp(solution2[0]),convertExp(solution2[1]))
				else:
					solution2Text='{} means {}\nwhich is False as by decoding the expression we get {} '.format(questionList[1],correctedExp2,convertExp(solution2[0]))	
			correctedExp3=convertExp(questionList[2])
			if answerList[2]==True:
				solution3Text='{} means {}\nwhich is True as by decoding the expression we get {} '.format(questionList[2],correctedExp3,convertExp(solution3[0]))
			else:
				if len(solution3)==2:
					solution3Text='{} means {}\nwhich is False as by decoding the expression we get that there is no direct relation between expressions {},{} '.format(questionList[2],correctedExp3,convertExp(solution3[0]),convertExp(solution3[1]))
				else:
					solution3Text='{} means {}\nwhich is False as by decoding the expression we get {} '.format(questionList[2],correctedExp3,convertExp(solution3[0]))			
			text+='\n{}.Statement:\n{}\nConclusion:\nI. {}\nII. {}\nIII. {}\n(1) If only conclusion I is true.\n(2) If only conclusion II is true.\n(3) If either conclusion I or II is true.\n(4) If neither conclusion I nor II is true.\n(5) If both the conclusions I and II are true.\nAnswer key: {}\nSolution:\n{}\n{}\n\n{}\n\n{}\n\n'.format(i,', '.join(expression_list),questionList[0],questionList[1],questionList[2],key,CommonSolutionText,solution1Text,solution2Text,solution3Text)
		

		else:
			print "Avoiding infiniteLoop"
		




	return text


countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	try:
		text=str('\nSet {}\n\n').format(sets_count+1)+mainProgram()
		#print "Set {}".format(i+1)
		global fn
		fn = os.path.join(os.path.dirname(__file__), 'sampleQuestions.txt')
		file = open(fn, "a")
	 	file.write(text.encode('utf8'))
	 	file.close()
	 	sets_count+=1
	except:
		print ('\n')+"Error in Set {}".format(sets_count+1)
		pass
print 'Done. Output written to file : {} '.format(fn)