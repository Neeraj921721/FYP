import csv
import fileinput
import linecache
import os
import collections
import sys
import csv
import numbers
import operator
from functools import cmp_to_key

class Atom:
	def __init__(self,condition,trueBranch,falseBranch):
		self.condition=condition
		self.trueBranch=trueBranch
		self.falseBranch=falseBranch
	
	def setCondition(self,condition):
		self.condition=condition
	
	def setTrueBranch(self,trueBranch):
		self.trueBranch=trueBranch
	
	def setFalseBranch(self,falseBranch):
		self.falseBranch=falseBranch
		
	def __repr__(self):#magic mathod
		return str(self.condition)+" "+str(self.trueBranch)+" "+str(self.falseBranch)
	
class Predicate:
	def __init__(self,rank=0,STarget=0.0,SObserved=0.0,fitness=0.0,text="",lineNo=0,atoms=[],atomCount=0,operatorScore=0,reachabilityScore=0.0):
		self.rank = rank
		self.STarget=STarget
		self.SObserved=SObserved
		self.fitness=fitness
		self.text = text
		self.lineNo = lineNo
		self.atoms=atoms
		self.atomCount=atomCount
		self.operatorScore=operatorScore
		self.reachabilityScore=reachabilityScore

	def setRank(self, rank):
		self.rank = rank 
	
	def setSTarget(self,STarget):
		self.STarget=STarget
	
	def setSObserved(self,SObserved):
		self.SObserved=SObserved
	
	def setFitness(self,fitness):
		self.fitness=fitness

	def setText(self, text):
		self.text = text

	def setLineNo(self,lineNo):
		self.lineNo = lineNo
		
	def setAtoms(self,atoms):
		self.atoms=atoms
	
	def setAtomCount(self,atomCount):
		self.atomCount=atomCount
		
	def setOperatorScore(self,operatorScore):
		self.operatorScore=operatorScore
		
	def setReachabilityScore(self,reachabilityScore):
		self.reachabilityScore=reachabilityScore
		
	def __repr__(self):
		return str(self.lineNo)+" "+str(self.suspiciousScore)+" "+str(self.rank)+" "+self.text;
	def __gt__(self, line2):
		return self.rank > line2.rank
		
		
	
def fetchPredicatesInCoverageReport(CBMCFile):
		predicates=[]
		with open(CBMCFile,"r") as file:
			flag=0
			prevLineNo=-1
			while True:
				line1=file.readline().strip()
				try:
					if len(line1)==0:
						if flag==0:
							flag=1
							file.readline()
						else:
							flag=0
							predicates.append(predicate)
							break
					elif flag==1:
						line2=file.readline().strip()
						line1Content=line1.split(' ')
						line2Content=line2.split(' ')
						line1No=int(line1Content[4])
						line2No=int(line2Content[4])
						
						if line1No!=prevLineNo:
							if prevLineNo!=-1:
								predicates.append(predicate)
							predicate=Predicate(0,0.0,0.0,0.0,"",line1No,[],0,0,0.0)
							prevLineNo=line1No
						
						trueBranch=0
						falseBranch=0
						if line1Content[12]=="SATISFIED":
							trueBranch=1
						if line2Content[12]=="SATISFIED":
							falseBranch=1
						atom=Atom(line1Content[8]+line1Content[9]+line1Content[10],trueBranch,falseBranch)
						predicate.atomCount+=1;
						predicate.atoms.append(atom)
				except ValueError:
					break
		return predicates
	
def readCprogramFile(p10):
		lineContent={}
		with open(p10,encoding='utf8') as file:
			for i,line in enumerate(file):
				lineContent[i+1]=line
		return lineContent
				
def getOperatorScore(andOpCount,orOpCount,mixOpCount):
	return 10*mixOpCount+5*andOpCount+5*orOpCount
	
def findOperatorScoreOfEachPredicate(predicates,lineContent):
		for predicate in predicates:
			text=lineContent[predicate.lineNo]
			predicate.text=text
			andOpCount=text.count("&&")
			orOpCount=text.count("||")
			mixOpCount=1 if (andOpCount>0 and orOpCount>0) else 0
			predicate.operatorScore=getOperatorScore(andOpCount,orOpCount,mixOpCount)
			

def findReachabilityScoreOfEachPredicate(predicates):
	for predicate in predicates:
		rScore=0
		for atom in predicate.atoms:
			if atom.trueBranch==1 and atom.falseBranch==1:
				rScore+=3
			elif atom.trueBranch==1 or atom.falseBranch==1:
				rScore+=2
			else:
				rScore+=1
		predicate.reachabilityScore=rScore
	
def getSTarget(atomCount,operatorScore):
	return atomCount/3.0+operatorScore/2.0+(3*atomCount)/1.0

def findSTargetOfEachPredicate(predicates):
	for predicate in predicates:
		predicate.STarget=getSTarget(predicate.atomCount,predicate.operatorScore)

def getSObserved(atomCount,operatorScore,reachabilityScore):
	return atomCount/3.0+operatorScore/2.0+reachabilityScore/1.0


def findSObservedOfEachPredicate(predicates):
	for predicate in predicates:
		predicate.SObserved=getSObserved(predicate.atomCount,predicate.operatorScore,predicate.reachabilityScore)

def getFitness(SObserved,STarget):
	return SObserved/STarget
	
def findFitnessOfEachPredicate(predicates):
	for predicate in predicates:
		predicate.fitness=getFitness(predicate.SObserved,predicate.STarget)

def myCompareFn(predicate1,predicate2):
		if predicate1.fitness<predicate2.fitness:
			return -1
		elif predicate1.fitness>predicate2.fitness:
			return 1
		elif predicate1.reachabilityScore<predicate2.reachabilityScore:
			return -1
		elif predicate1.reachabilityScore>predicate2.reachabilityScore:
			return 1
		elif predicate1.operatorScore<predicate2.operatorScore:
			return -1
		elif predicate1.operatorScore>predicate2.operatorScore:
			return 1
		elif predicate1.atomCount<predicate2.atomCount:
			return -1
		elif predicate1.atomCount>predicate2.atomCount:
			return 1
		return 0
		
def assignRank(predicates):
	prev=None
	rank=0
	for predicate in predicates:
		if prev is None:
			rank+=1
			predicate.rank=rank
		else:
			if prev.fitness==predicate.fitness and prev.atomCount==predicate.atomCount and prev.operatorScore==predicate.operatorScore and prev.reachabilityScore==predicate.reachabilityScore:
				predicate.rank=rank
			else:
				rank+=1
				predicate.rank=rank
		prev=predicate


def writeToOutputFile(fileWriter,lines):
	fileWriter.write("LineNo\t\tRank\t\tFitness\t\tSObserved\tSTarget\t\tReachabilityScore\t\tOperatorScore\t\tAtomCount\t\t\tLine of code\n")
	fileWriter.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	for predicate in predicates:
		fileWriter.write(str(predicate.lineNo)+"\t\t"+str(predicate.rank)+"\t\t"+str(round(predicate.fitness,4))+"\t\t"+
			str(round(predicate.SObserved,4))+"\t\t  "+str(round(predicate.STarget,4))+"\t\t\t"+str(predicate.reachabilityScore)+"\t\t\t"+
			str(predicate.operatorScore)+"\t\t\t"+str(predicate.atomCount)+"\t\t\t"+str(predicate.text))	
		
#read CBMC(coverage report file) name
CBMCFile=sys.argv[1]
#predicates is list of predicate object
predicates=fetchPredicatesInCoverageReport(CBMCFile)
#sort predicates list based on line No
predicates=sorted(predicates,key=lambda x:x.lineNo)#key=operator.attrgetter('lineNo')


#read content of C program line by line
p10=sys.argv[2]
#lineContent is a dict (key:lineNo val:lineString)
lineContent=readCprogramFile(p10)
'''for key,val in lineContent.items():
	print(str(key)+" "+val)
'''
#read output file name
outputFile=sys.argv[3]

#Find Operator Type(&&/||/(mix of && and ||)
findOperatorScoreOfEachPredicate(predicates,lineContent)

#ReachabilityScore of predicates based on it's atomic condition's reachability
findReachabilityScoreOfEachPredicate(predicates)

#find STarget(Target suspicious score)
findSTargetOfEachPredicate(predicates)

#find SObserved(Observed suspicious score)
findSObservedOfEachPredicate(predicates)

#find fitness(fitness score)
findFitnessOfEachPredicate(predicates)
'''
for predicate in predicates:
	print(str(predicate.lineNo)+" "+str(predicate.fitness)+" "+str(predicate.reachabilityScore)+" "+str(predicate.operatorScore))

'''
#sort predicates based on #1)fitness,2)reachabilityScore,3)operatorScore,4)atomicCount
predicates=sorted(predicates,key=cmp_to_key(myCompareFn),reverse=True)

#assign rank to each predicate
assignRank(predicates)

#print output to OutputFile
fileWriter=open(outputFile,'w')
writeToOutputFile(fileWriter,predicates)


'''
for line in lines:
	print(str(line.rank)+" "+str(line.lineNo)+" "+str(line.atomCount)+" "+str(line.operatorType)+" "+str(line.reachabilityScore))

'''









