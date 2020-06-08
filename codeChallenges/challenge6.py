#challenge6
#https://www.linkedin.com/learning/python-code-challenges/save-a-dictionary?u=2163426

#?
#write function to sort the words in a string

""" My attempt - doesn't work, but valiant effort:

#Save a dictionary to file
#Input: dictionary to save & output file path
def saveD(dictOut, fileOutPath):
	with open(fileOutPath, 'wt') as fileOut:
		for key in dictOut.keys():
			print(key + "," + str(dictOut[key]), file=fileOut)

#load function 
#input: file path to saved dictionary
#output: loaded dictionary
def loadD(fileInPath):
	dictIn = {}
	with open(fileInPath, 'rt') as fileIn:
		for lineF in fileIn:
			columns = lineF.split(',')
			dictIn[columns[0]] = columns[:1] #or [:1]?
	return dictIn
"""

#url in the video from above url doesn't work; use this:
#https://docs.python.org/3/library/pickle.html
import pickle

def saveD(dictOut, fileOutPath):
	with open(fileOutPath, 'wb') as fileOut:
		pickle.dump(dictOut, fileOut)

def loadD(fileInPath):
	with open(fileInPath, 'rb') as fileIn:
		return pickle.load(fileIn)

def getDict():
	dict = {'a': '1', 'b': 2, 'c': '3'}
	return dict
	
def getPath():
	return "challenge6.pickle"
	
#main:
saveD(getDict(), getPath())
print("saved dictionary")
#input("Verify and hit enter to continue...")
myDict = loadD(getPath())
print("loaded dictionary:")
print(myDict)

