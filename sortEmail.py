#sortEmail

def sortEmail(fileInPath, fileOutPath):
	dataIn = list()
	emoryEdu = list()
	emoryHealthcare = list()
	edus = list()
	emoryOther = list()
	govs = list()
	coms = list()
	nets = list()
	orgs = list()
	with open(fileInPath, "rt") as fileIn:
		dataIn = fileIn.readlines()
	for	lineIn in dataIn:
		if lineIn.strip().endswith("@emory.edu"):
			emoryEdu.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith("@emoryhealthcare.org"):
			emoryHealthcare.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith(".edu"):
			edus.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith(".gov"):
			govs.append(lineIn)
			dataIn.remove(lineIn)
		elif "emory" in lineIn:
			emoryOther.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith(".com"):
			coms.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith(".net"):
			nets.append(lineIn)
			dataIn.remove(lineIn)
		elif lineIn.strip().endswith(".org"):
			orgs.append(lineIn)
			dataIn.remove(lineIn)
	
	#TODO: Why sometimes .endswith("@emory.edu") works and sometimes doesn't?
	
	with open(fileOutPath, "wt") as fileOut:
		fileOut.write("@emory.edu=====================================================\n")
		for lineOut in emoryEdu:
			fileOut.write(lineOut)

		fileOut.write("@emoryHealthcare===============================================\n")
		for lineOut in emoryHealthcare:
			fileOut.write(lineOut)

		fileOut.write("Other .edu=====================================================\n")
		for lineOut in edus:
			fileOut.write(lineOut)

		fileOut.write(".gov===========================================================\n")
		for lineOut in govs:
			fileOut.write(lineOut)

		fileOut.write("Emory Other====================================================\n")
		for lineOut in emoryOther:
			fileOut.write(lineOut)

		fileOut.write(".com===========================================================\n")
		for lineOut in coms:
			fileOut.write(lineOut)

		fileOut.write(".net===========================================================\n")
		for lineOut in nets:
			fileOut.write(lineOut)

		fileOut.write(".org===========================================================\n")
		for lineOut in orgs:
			fileOut.write(lineOut)
		
		fileOut.write("Etc============================================================\n")
		for lineOut in dataIn:
			fileOut.write(lineOut)

	#print()
	#print("dataIn length: " + str(len(dataIn)))
	#print("emoryEdu length: " + str(len(emoryEdu)))
	#print("edus length: " + str(len(edus)))
	#print("emoryOther length: " + str(len(emoryOther)))
	#print("govs length: " + str(len(govs)))
	print("Done")

#main
fileInPath = "email_emory_in.txt"
fileOutPath = "email_emory_out.txt"
sortEmail(fileInPath, fileOutPath)