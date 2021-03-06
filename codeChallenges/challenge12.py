#challenge12
#https://www.linkedin.com/learning/python-code-challenges/merge-csv-files?u=2163426

#Merge multiple csv files into one, even if the headers don't match or headers are in wrong order

import csv

#input: list of file paths to merge, output file path
def mergeCSV(fileList, outFile):
	#1: get fieldNames
	fieldNames = list()
	for filePath in fileList:
		with open(filePath, "rt") as fileIn:
			fn = csv.DictReader(fileIn).fieldnames
			fieldNames.extend(x for x in fn if x not in fieldNames)
	
	#2: get data
	with open(outFile, "wt", newline="") as fileOut:
		writer = csv.DictWriter(fileOut, fieldnames = fieldNames)
		writer.writeheader()
		for filePath in fileList:
			with open(filePath, "rt") as fileIn:
				reader = csv.DictReader(fileIn)
				for row in reader:
					writer.writerow(row)

	#bonus: remove lines where first value is a duplicate
	"""TODO
	keyNames = list()
	rows = list()
	with open(outFile, "rt", newline="") as fileIn:
		reader = csv.DictReader(fileIn)
		for key, value in reader:
			if key not in keyNames:
				keyNames.append(key)
				rows.append(value)
			else:
				print("excluding duplicate: " + key)
			
	with open("challenge12_final.txt", "wt", newline="") as fileOut:
		writer = csv.DictWriter(fileOut, fieldnames = fieldNames)
		writer.writeheader()
		for row in rows:
			writer.writerow(row)
	"""
#main
mergeCSV(["challenge12_1.txt","challenge12_2.txt"], "challenge12_out.txt")