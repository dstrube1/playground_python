"""
Exploring different ways of finding fibonacci numbers
using python 3 syntax

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1
"""

import sys

#Solution 0 - must test on 0,1,2,3,'x', and None
def fib(num0): #logic error, must investigate
	#input datatype checking
	if not isinstance(num0, int):
		print('Input should be of Integer type')
		return
	if num0 <= 0:
		return 0
	fibo = (0+1) * [0]
	#fibo[1] = 1 #IndexError: list assignment index out of range
	fibo.append(1)
	s = fibo[1] + fibo[0]
	for i in range(2, num0 + 1):
		#fibo[i] = fibo[i - 2] + fibo[i - 1]#IndexError: list assignment index out of range
		fibo.append(fibo[i - 2] + fibo[i - 1])
		s += fibo[i]
	return s

#Solution 1
class Solution:
	def fib1(self, num1: int) ->  int:
		#is isinstance valid here?
		#yes, the above decorator is only a decorator, not a contract
		if not isinstance(num1, int):
			print('Input should be of Integer type')
			return
		if num1 <= 0: 
			return 0
		elif num1 == 1:
			return 1
		return self.getFib(num1)
	
	def getFib(self, N: int) -> int:
		cache = {0: 0, 1: 1}
		for i in range(2, N+1):
			cache[i] = cache[i-1] + cache[i-2]
		return cache[N]

	#Solution #2
	def fib2(self,num2:int) -> int:
		if not isinstance(num2, int):
			print('Input should be of Integer type')
			return
		if num2 <= 0:
			return 0;
		elif num2 == 1:
			return num2
		else:
			return self.fib2(num2 - 1) + self.fib2(num2 - 2) if num2 > 1 else num2

	#Solution #3
	def fib3(self, num3:int) -> int:
		if not isinstance(num3, int):
			print('Input should be of Integer type')
			return
		if num3 <= 0:
			return 0
		
		if num3 in [0,1]:
			return num3
		first,second,result = 0,1,0
		for i in range(2, num3 + 1):
			result = first + second
			second = first
			first = result
		return first + second
		
def main(args):
	print("testing with 0,1,2,3,'x', and None")
	fibMax = 8
	
	"""
	#Function fib needs work
	for i in range(0, fibMax):
		print(str(i) + " : " + str(fib(i)))
	print(str('x') + " : " + str(fib('x')))
	print(str(None) + " : " + str(fib(None)))"""
	
	s = Solution()
	
	#fib1 works great
	"""for i in range(0, fibMax):
		print(str(i) + " : " + str(s.fib1(i)))
	print(str('x') + " : " + str(s.fib1('x')))
	print(str(None) + " : " + str(s.fib1(None)))"""
	
	#fib2 works great
	"""for i in range(0, fibMax):
		print(str(i) + " : " + str(s.fib2(i)))
	print(str('x') + " : " + str(s.fib2('x')))
	print(str(None) + " : " + str(s.fib2(None)))"""
	
	#fib3 works great
	for i in range(0, fibMax):
		print(str(i) + " : " + str(s.fib3(i)))
	print(str('x') + " : " + str(s.fib3('x')))
	print(str(None) + " : " + str(s.fib3(None)))

if __name__ == '__main__':
    main(sys.argv)