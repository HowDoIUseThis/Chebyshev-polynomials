# -*- coding: utf-8 -*-
"""
Chebyshev Node calculations

@author: Chris
"""
import math
import matplotlib.pyplot as plt


def getNodes(degree):
	tempList = []	
	for x in range(degree+1):
		if x != 0:
			temp = math.cos((2*(x) -1)*math.pi/(2*degree))
			if math.isclose([temp,1.e-8],[0.,1.e-8]):
				tempList.append(0)
			else:
				tempList.append(temp)
				print(temp)
	return tempList
	
	
def plotNodes(listOfNodes):
	pass

def listToDegOf(maxDeg):
	fullList = []
	for x in range(maxDeg):
		fullList.append(getNodes(x))
	return fullList
	

test = listToDegOf(4)
print(test)