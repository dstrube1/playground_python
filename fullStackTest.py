#fullStackTest.py

"""
#1
def extendList(val,list=[]):
	if(len(list)>0):
		list = []
	list.append(val)
	return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

1a:
python3: syntax error
python2:
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']

1b: either remove option for default value or check length of list and set it to empty if len>0
"""

"""
#2
from functools import partial
def multipliers():
	#solution 1: return [partial(lambda y,x : x * y, i) for i in range(4)]
	#solution 2: return [lambda x, coef=i: coef * x for i in range(4)]
	
print [m(2) for m in multipliers()]
"""

"""#3
class Parent(object):
	x = 1
class Child1(Parent):
	pass
class Child2(Parent):
	pass
print Parent.x, Child1.x, Child2.x #1 1 1
Child1.x = 2
print Parent.x, Child1.x, Child2.x #1 2 1
Parent.x = 3
print Parent.x, Child1.x, Child2.x #3 2 1
"""

"""
#4
def div1(x,y):
	#print "%s/%s = %s" % (x,y,x/y)
	print("%s/%s = %s" % (x,y,x/y)) #2.5
def div2(x,y):
	#print "%s//%s = %s" % (x,y,x//y)
	print("%s//%s = %s" % (x,y,x//y)) #2
div1(5,2) #5/2 = 2
div1(5,2) #5/2 = 2
div2(5,2) #5//2 = 2
div2(5.,2.) #5.0//2.0 = 2.0
"""

"""#5
list = ['a','b','c','d','e']
print list[10:] #[]"""

"""#6
list = [[]] * 5
list #[[], [], [], [], []]
list[0].append(10)
list #[[10], [10], [10], [10], [10]]
list[1].append(20)
list #[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
list.append(30)
list #[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
"""

"""
#7
list0 = [1,2,2,4,6]
list1 = [list0[x] for x in range(len(list0)) if (x%2 == 0 and list0[x]%2 == 0) ]
print list1
#"""

"""#8
class DefaultD(dict):
	#pass
	def __missing__(self, key):
		return []
d = DefaultD()
d['bleh'] = 127
print d['bleh']
"""

"""#9
name = None
line = 1
#print(len(name), line)
#check for None, len?
"""

"""#10
import math
print dir(math)"""

#11

from itertools import permutations

def findLeast(listA):
	candidate = 1
	sums = []
	subsetSums(listA, 0, len(listA)-1, sums)
	sums = sorted(list(set(sums)))
	#from https://stackoverflow.com/questions/21105317/making-list-of-all-possible-sums-up-to-a-certain-value
	while True:
		if candidate in sums:
			candidate += 1
		else:
			return candidate
			
def subsetSums(listB, left, right, sums, sum = 0): 
	#from https://www.geeksforgeeks.org/print-sums-subsets-given-set/
    if left > right: 
        sums.append(sum)
        return
  
    # Subset including listB[left] 
    subsetSums(listB, left + 1, right, sums, sum + listB[left])
  
    # Subset excluding listB[left] 
    subsetSums(listB, left + 1, right, sums, sum)
a = [1,2,5,7]
print("least = ", findLeast(a))
b = [1,2,2,5,7]
print("least = ", findLeast(b))

