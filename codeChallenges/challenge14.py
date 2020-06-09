#challenge14
#https://www.linkedin.com/learning/python-code-challenges/build-a-zip-archive?u=2163426

#Build a zip archive
#4 star difficulty

import os
from zipfile import ZipFile

#input: directory to zip, list of file extension, output file path

#zip archive should maintain folder structure relative to top level directory
def zipAll(directory, fileExtList, outPath):
	#if os.path.isfile(outPath):
	#	mode = 'a'
	#else:
	#	mode = 'w'
	#If 'a' creates a file when no file exists, why would I ever want to use 'w'? 
	#https://docs.python.org/3/library/zipfile.html
	
	with ZipFile(outPath, 'w') as myzip:
		for root, dirs, files in os.walk(directory):
			relPath = os.path.relpath(root, directory)
			for file in files:
				name, ext = os.path.splitext(file)
				if ext.lower() in fileExtList:
					myzip.write(os.path.join(root, file),
						arcname = os.path.join(relPath, file))
	
#main
fileExts = [".txt", ".py"]
zipAll("../../playground_python/.", fileExts, "out.zip")
