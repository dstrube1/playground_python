#websiteUpdateTracker.py

import os.path
import os
import datetime
import requests
import sys
import time
import datetime
import threading

url1 = "https://www.gnrhealth.com/no-appts-available/"
url2 = "https://www.gnrhealth.com/covid-vaccine-scheduling/"

def lastReadFileExists(lastReadFile):
	if os.path.isfile(lastReadFile):
		#print ("Last read file exist")
		return True
	else:
		print ("Last read file not exist")
		return False

def createLastReadFile(filePath, url):
	with open(filePath, "wt") as fileOut:		
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			response = requests.get(url, headers = headers)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
			print("Caught exception while trying to create last read file")
			return
		fileOut.write(response.text)

def getTime():
	timeFormat = "%H:%M:%S"
	return datetime.datetime.now().strftime(timeFormat)

def getTimeForFile():
	timeFormat = "%H-%M-%S"
	return datetime.datetime.now().strftime(timeFormat)
	
def getLatest(num, url):
	if num == 1:
		newLastReadFilePrefix = "websiteUpdateTracker_1_"
		url = url1
	else:
		newLastReadFilePrefix = "websiteUpdateTracker_2_"
		url = url2
	newLastReadFileSuffix = ".txt"
	newLastReadFile = newLastReadFilePrefix + getTimeForFile() + newLastReadFileSuffix
	createLastReadFile(newLastReadFile, url)
	return newLastReadFile
	
def areDiff(file1, file2):
	with open(file1, "rt") as fileIn1:
		dataIn1 = fileIn1.readlines()
	with open(file2, "rt") as fileIn2:
		dataIn2 = fileIn2.readlines()
	if len(dataIn1) != len(dataIn2):
		print(file1 + " len = " + str(len(dataIn1)))
		print("!=")
		print(file2 + " len = " + str(len(dataIn2)))
		index = 0
		if len(dataIn1) < len(dataIn2):
			for lineX in dataIn1:
				if dataIn2[index] != lineX:
					print("At line " + str(index) + ":")
					print(dataIn2[index]) 
					print("!=")
					print(lineX)
					return True
				else:
					index += 1
		else :
			for lineX in dataIn2:
				if dataIn1[index] != lineX:
					print("At line " + str(index) + ":")
					print(dataIn1[index]) 
					print("!=")
					print(lineX)
					return True
				else:
					index += 1
		return True
	return False

def playsound(soundFile):
	os.system("afplay " + soundFile) 

def deletePrevRun():
	path = '.'
	files = os.listdir(path)
	for f in files:
		if "websiteUpdateTracker_1_" in f or "websiteUpdateTracker_2_" in f:
			#print("Deleting " + f + "...")
			os.remove(f)

#main
def main(args):
	lastReadFile1 = "websiteUpdateTracker_1.txt"	
	lastReadFile2 = "websiteUpdateTracker_2.txt"
	
	alarmFilePath = "codeChallenges/challenge7.mp3"
	
	if not lastReadFileExists(lastReadFile1):
		createLastReadFile(lastReadFile1, url1)
	
	if not lastReadFileExists(lastReadFile2):
		createLastReadFile(lastReadFile2, url2)
	
	while(True):
		#wait 3 minutes
		#thread = threading.main_thread()
		minutes = 3
		print("Waiting for " + str(minutes) + " minutes, starting at " + getTime() + "...")
		time.sleep(minutes * 60)
		#delete previous runs
		deletePrevRun()
		#get latest
		newLastReadFile1 = getLatest(1, url1)
		newLastReadFile2 = getLatest(2, url2)
		#compare to last read
		if areDiff(lastReadFile1, newLastReadFile1) or areDiff(lastReadFile2, newLastReadFile2):
			if areDiff(lastReadFile1, newLastReadFile1):
				print(lastReadFile1 + " != " + newLastReadFile1)
			else:
				print(lastReadFile2 + " != " + newLastReadFile2)
			playsound(alarmFilePath)
			return

if __name__ == '__main__':
    main(sys.argv)