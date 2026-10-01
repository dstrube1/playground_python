# phoneNumberPuzzle.py
"""
from here:
https://www.youtube.com/shorts/ausLKMojXaY
Math fact: 
Given any valid phone number P (10 digits), it possible to find another number bigger than 0 A,
such that if you multiply P by A, it gives you a bigger number that is all 0s and 1s

Also, if the number ends in 1, 3, 7, or 9, 
then it's possible to find a number whose every digit is just a 1.
(Interesting: if the number doesn't end in one of those numbers, 
does that mean it's impossible to find such a product?)
Goal of the puzzle: prove why this is true.

My first goal: explore this fact.
Warning: just finding the number by brute force will probably take too much computation. 
Must be a little clever here.
"""

import sys

# Some numbers to try:
P_of_now = 4048675309
P_default = 2222222222
max_P = 9999999999
add_to_P = 1111111111
min_binary = "1000000000"

"""
My first step in thinking about this: for each number from 0-9, 
what are all the possible first digits of products from that number?

0 => 0
1 => 0,1,2,3,4,5,6,7,8,9
2 => 0,2,4,6,8
3 => 0,3,6,9,2,5,8,1,4,7
4 => 0,4,8,2,6
5 => 0,5
6 => 0,6,2,8,4
7 => 0,7,4,1,8,5,2,9,6,3
8 => 0,8,6,4,2
9 => 0,9,8,7,6,5,4,3,2,1

1,3,7,9
"""

def nextBinary(num):
	# Takes in something that might be numeric, might be string
	# Returns next binary as string
	# Returns 0 if input is not binary
	if not isOnly1sAnd0s(num): 
		print("ERROR: this is not binary: " + num)
		return 0
	num_str = str(num)
	if num_str[0] == '0':
		num_str[0] = '1'
		return num_str
	else:
		dec_num = int(num, 2)
		dec_num += 1
		bin_num = bin(dec_num)[2:] # remove the "0b" prefix
		return bin_num
		

def isOnly1sAnd0s(num):
	num_str = str(num)
	for n in num_str:
		if n == '1' or n == '0':
			continue
		else:
			return False
	return True

# How long does a single brute force search take?
# For 2222222222, not long
# For P_default + add_to_P, too long
def foreachNumOld(num_to_test):
	factor = 1
	while not isOnly1sAnd0s(num_to_test * factor):
		factor = factor + 1
	print("Found that " + str(num_to_test) + " * " 
		+ str(factor) + " = " + str(num_to_test * factor))

def mainOld(args):
	test_num = P_default
	while test_num < max_P:
		# This quickly finds that 2222222222 * 5 = 11111111110
		# but after that, P_default + add_to_P takes too long
		# TODO: find more efficient logic
		foreachNumOld(test_num)
		test_num += add_to_P

def foreachNum(num_to_test):
	next_bin = min_binary
	#print("In foreachNum, next_bin = " + next_bin)
	my_count = 0
	while int(next_bin) % num_to_test != 0:
		#if next_bin == "11111111110":
		#	print("next_bin (" + next_bin + ") % num_to_test (" + str(num_to_test) + ") = " + str(int(int(next_bin) % num_to_test)))
		#my_count += 1
		#if my_count % 10000 == 0:
		#	print("testing " + next_bin)
		#	return
		next_bin = nextBinary(next_bin)
		
	#print("num_to_test (" + str(num_to_test) + ") % next_bin (" + next_bin + ") == 0 ?: " + str(num_to_test % int(next_bin, 2)))
	quotient = int(next_bin) / num_to_test
	print(str(num_to_test) + " * " 
		+ str(int(quotient)) + " = " + next_bin + " : " + str(int(quotient * num_to_test)))
	

def main(args):
	test_num = P_default 
	#print("Starting with test_num = " + str(test_num))
	while test_num < max_P:
		foreachNum(test_num)
		test_num += add_to_P

if __name__ == '__main__':
    main(sys.argv)


#2222222222 * 5 = 11111111110 : 11111111110
#3333333333 * 33333333336666664960 = 111111111111111111111111111111 : 111111111111111105501764517888
#4444444444 * 25 = 111111111100 : 111111111100
#5555555555 * 2 = 11111111110 : 11111111110


























