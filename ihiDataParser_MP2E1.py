#ihiDataParser_MP2E1.py

#Parser of data for CS6440 - Introduction to Health Informatics 
#	Mini Project #2, exercise 1

#Usage: python ihiDataParser_MP2E1.py {fileIn}.txt
#fileIn.txt is the input file that is parsed

#Output: fileOut.txt: contains the data that has been parsed

import os.path
import os
import sys

#This is a temporary file path. Gets overwritten every time this is successfully run
fileOutPath = "fileOut.txt"

#Parse data from the Rate column
def parseRate(dataIn):
	print("parseRate")
	outs = list()
	for lineX in dataIn:
		rates = lineX.split(" ")
		for rate in rates:
			#print("Appending " + rate)
			outs.append(rate)
	with open(fileOutPath, "wt") as fileOut:
		for out in outs:
			if "Rate" in out:
				continue
			if "\n" in out:
				fileOut.write(out)
			else:
				fileOut.write(out + "\n")

#Parse data from the Number & Percent of total deaths columns
def parseNums(dataIn):
	print("parseNums")
	ints = list()
	floats = list()
	for lineX in dataIn:
		if not lineX[:1].isnumeric():
			continue
		numsInLine = lineX.split(" ")
		for num in numsInLine:
			if "." in num:
				floats.append(num)
			else:
				ints.append(num)
	with open(fileOutPath, "wt") as fileOut:
		for i in ints:
			fileOut.write(i + "\n")
		fileOut.write("\n")
		for f in floats:
			fileOut.write(f + "\n")

#Parse data from the Cause of death column
def parseCause(dataIn):
	#Note: At page 8, I had to split of source text copies, presumably due to size of one of the columns
	print("parseCause")
	outs = list()
	for lineX in dataIn:
		if lineX.startswith("Cause of death"):
			continue
		if lineX.startswith("..."):
			lineX = lineX[4:]
		elif lineX[:1].isnumeric():
			if lineX[:2].isnumeric():
				lineX = lineX[3:]
			else:
				lineX = lineX[2:]
		else:
			pass
		outs.append(lineX)
	with open(fileOutPath, "wt") as fileOut:
		for out in outs:
			fileOut.write(out)

#Parse data from the Number & Percent of total deaths & Rate columns
def parse3Cols(dataIn):
	#This became necessary at page 5.
	#At page 6, I learned that if this is not necessary, it's not an option- 
	#input is in a different format in that case.
	#I had to modify the condition so that it's not dependent on the second line.
	#But that wasn't good enough- had to modify how I capture the second line 
	#so that the first line in input didn't include the first line condition for this 
	#function, so that we would call the old parseNums instead.
	print("parse3Cols")
	col1 = list()
	col2 = list()
	col3 = list()
	countCol = 0
	for lineX in dataIn:
		if not lineX[:1].isnumeric():
			continue
		numsInLine = lineX.split(" ")
		for num in numsInLine:
			countCol += 1
			if countCol % 3 == 1:
				col1.append(num)
			elif countCol % 3 == 2:
				col2.append(num)
			else:
				col3.append(num)
	with open(fileOutPath, "wt") as fileOut:
		for c1 in col1:
			fileOut.write(c1 + "\n")
		fileOut.write("\n")
		for c2 in col2:
			fileOut.write(c2 + "\n")
		fileOut.write("\n")
		for c3 in col3:
			fileOut.write(c3 + "\n")

#main
def main(args):
	if len(args) < 2:
		print("Error: Call must include input file")
		return
	#args[0]: name of calling file
	#print("args[0]:" + args[0])
	fileInPath = args[1]
	with open(fileInPath, "rt") as fileIn:
		dataIn = fileIn.readlines()
	
	if "Rate" in dataIn[0]:
		parseRate(dataIn)
	elif "Cause of death" in dataIn[0]:
		parseCause(dataIn)
	elif "Percent of" in dataIn[0] : #and "Number total deaths Rate" in dataIn[1]:
		parse3Cols(dataIn)
	else:
		parseNums(dataIn)
	print("Done")
	

if __name__ == '__main__':
    main(sys.argv)