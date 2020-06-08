#challenge4
#https://www.linkedin.com/learning/python-code-challenges/find-all-list-items

"""first pass, doesn't handle nested lists
#function to give all indices of a given item in a list
def indexAll(inList, searchFor):
	indices = list()
	index = 0
	for item in inList:
		if item == searchFor:
			indices.append(index)
		index += 1
	return indices
"""

#This works well with multilayered lists, but not as well for a 1-dimensional list
def indexAll(inList, item):
	indices = list()
	for indexOuter in range(len(inList)):
		if inList[indexOuter] == item:
			indices.append([indexOuter])
		elif isinstance(inList[indexOuter], list):
			for indexInner in indexAll(inList[indexOuter], item):
				indices.append([indexOuter]+indexInner)
	return indices

inList = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7)
#https://www.piday.org/million/
indexOf = 3
print("in this list: " + str(inList))
print("indices of " + str(indexOf) + ": ")
print(str(indexAll(inList, indexOf)))

#what about multilayered lists:
inList = [[[1,2,3], 2, [1,3]], [1,2,3]]
indexOf = 2
print("in this list: " + str(inList))
print("indices of " + str(indexOf) + ": ")
#should be [[0,0,1], [0,1], [1,1]]
print(str(indexAll(inList, indexOf)))

#what if input is a list?
indexOf = [1,2,3]
print("in this list: " + str(inList))
print("indices of " + str(indexOf) + ": ")
print(str(indexAll(inList, indexOf)))
#Neat