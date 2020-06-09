#challenge15
#https://www.linkedin.com/learning/python-code-challenges/download-sequential-files?u=2163426

#Download sequential files
#4 star difficulty

import os
import re
import urllib.parse
import urllib.request

#input: url for first item, output dir path
#go until 404

def downloadFiles(url, folder):
	if not os.path.isdir(folder):
		os.mkdir(folder)
	urlHead, urlTail = os.path.split(url)
	firstIndex = re.findall(r'[0-9]+', urlTail)[-1]
	indexCount, errorCount = 0,0
	while errorCount < 5:
		nextIndex = str(int(firstIndex) + indexCount)
		if firstIndex[0] == '0': #zero padded
			nextIndex = '0' * (len(firstIndex) - len(nextIndex)) + nextIndex
		nextUrl = urllib.parse.urljoin(urlHead, re.sub(firstIndex, nextIndex, urlTail))
		try:
			outFile = os.path.join(folder, os.path.basename(nextUrl))
			urllib.request.urlretrieve(nextUrl, outFile)
			print("Successfully downloaded " + os.path.basename(nextUrl))
		except IOError:
			print("Could not retrieve " + nextUrl)
			errorCount += 1
		indexCount += 1

#main
firstUrl = "http://699340.youcanlearnit.net/image001.jpg" #-> 050
outFolder = "images"

downloadFiles(firstUrl, outFolder)