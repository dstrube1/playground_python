#makeUnique

in1 = ""
in2 = ""
out = ""

def uniqueify(fileList):
	dataIn = list()
	dupeCount = 0
	uniqueCount = 0
	for fileItem in fileList:
		with open(fileItem, "rt") as fileIn:
			for lineIn in fileIn.readlines():
				lineIn = lineIn.lower()
				if lineIn not in dataIn:
					dataIn.append(lineIn)
					uniqueCount += 1
				else:
					dupeCount += 1
	print("This many unique: " + str(uniqueCount))
	print("This many duplicates: " + str(dupeCount))
	with open(out, "wt") as fileOut:
		for lineOut in dataIn:
			fileOut.write(lineOut)
	print("Done")
#main
files = list()
files.append(in1)
files.append(in2)
uniqueify(files)