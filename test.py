#test.py
#Author: David Strube
#Date: 2015-12-30
#What is: testing python stuffs

dictionary = {
        'a': 1,
        'b': 2,
    }
def caseF(x):
    return dictionary.get(x, 9)    # 9 is default if x not found
    #also, don't declare the dictionary in the function, so as to not have to rebuild it everytime the function is called
#print caseF('a') #should return 1
#print caseF('c') #not found, should return default 9

def multiReturn():
	return 1,2

a=0
b=1
#print "a = ",a,"; b=",b #print initial values
a,b = multiReturn()
#print "a = ",a,"; b=",b #confirm behaves as expected
a=0
b=1
#print "a = ",a,"; b=",b #print resetted values
a = multiReturn() #if only one variable is the recipient of multiple values, that variables gets all the values
#print "a = ",a,"; b=",b

def noValueReturned(a,b):
	a = a+b
	
#print noValueReturned(1,2) #prints "None"
#make sure this didn't affect a&b above:
#print "a = ",a,"; b=",b 

def ifelseF():
	a = 1
	if a == 1:
		print('a is 1')
	elif a == 2: #else if => elif
		print('a is 2')
	else:
	#pass does nothing; used when a statement is required syntactically but the program requires no action.
		pass
#ifelseF()

def paramF(a,b=1,c='c'):
	print("a = ",a,"; b = ",b,"; c = ",c)
	print("a = {}; b = {}, c = {}".format(a,b,c))
#paramF() must be called with at least one param
#paramF(1) #1st param can be int
#paramF('x') #1st param can be string
#paramF(1,c=2,b='d') #params can be out of order if named; data types can change

import datetime
import time
def timeTest():
	now = datetime.datetime.now()
	current_local = time.localtime()
	#https://stackoverflow.com/questions/31299580/python-print-the-time-zone-from-strftime
	applyTimezoneName = current_local.tm_zone #time.struct_time.tm_zone #datetime.tzinfo.tzname(now.astimezone())
	applyTime = "{:02d}".format(now.hour) + ":" + "{:02d}".format(now.minute) + ":" + "{:02d}".format(now.second)
	applyDate = str(now.year) + "-" + "{:02d}".format(now.month) + "-" + "{:02d}".format(now.day)
	print("datetime to apply: " + applyDate + " " + applyTime + " " + applyTimezoneName)	
#timeTest()

def rangeTest():
	print("range(0,3):")
	for x in range(0,3):
		print(x) #0,1,2
	
	print("range(1,4):")
	for x in range(1,4):
		print(x) #1,2,3
#rangeTest()

def createStaircase(nums):
	"""INCORRECT:
	while len(nums) != 0:
		step = 1
		subsets = []
		if len(nums) > step:
			subsets.append(nums[0:step])
			nums = nums[step:]
			step += 1
		else:
			return False
	return True"""
	step = 1
	subsets = []
	while len(nums) != 0:
		if len(nums) >= step:
			subsets.append(nums[0:step])
			nums = nums[step:]
			step += 1
		else:
			return False
	return subsets

#print (createStaircase([1,2,3,4,5,6]))

from bs4 import BeautifulSoup
# pip install bs4
import requests

def printFromURL(url):
	try:
		# got this much from emailScraper:
		response = requests.get(url) 
		#print(response.text)
		soup = BeautifulSoup(response.text, features="html.parser") 
		#tables = soup.find_all("table")
		#print(tables)
		
		# this is from here:
		# https://stackoverflow.com/questions/45843025/parsing-html-tables-with-beautifulsoup-in-python
		table_data = [i.text for i in soup.find_all('td')]
		
		# throw away the header row
		table_data = table_data[3:]
		#print(table_data)
		
		# Convert list into coordinate-character pairs
		points = [(int(table_data[i]), int(table_data[i+2]), table_data[i+1]) for i in range(0, len(table_data), 3)]
		print (points)
		
		if len(points) == 0:
			print("Points is empty")
			return
		
		# Determine grid size
		max_x = max(x for x, y, char in points)
		max_y = max(y for x, y, char in points)
		
		# Create grid with default space character
		grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
		
		# Fill grid with characters
		for x, y, char in points:
			grid[y][x] = char
		
		# Print the grid
		for row in grid:
			print(''.join(row))
		
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		print("Caught exception")

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
printFromURL(url)

print([x * 2 for x in range(3)])
