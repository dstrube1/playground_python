#challenge0

#determine if a string is a palindrome
#input: string to evaluate
#output: boolean
#only consider letters (if contains non letter, return false or throw error?)
#ignore case

#My solution:
def isPalindrome(input):
	input = input.lower()
	testing1 = ""
	for c in input:
		if c.isalpha():
			testing1 += c
	#print("testing " + testing1)
	reversed = testing1[::-1]
	#print("reversed: " + reversed)
	if testing1 == reversed:
		return True
	return False

#Instructor's solution, more compact, but requires regular expression library:
import re
def is_palindrome(input):
	#join used to merge list of results into a string
	forwards = ''.join(re.findall(r'[a-z]+', input.lower()))
	backwards = forwards[::-1]
	return forwards == backwards

input = "Hello world."
print("isPalindrome("+input+"): " + str(isPalindrome(input)))
print("is_palindrome("+input+"): " + str(is_palindrome(input)))

input = "I man am regal. A German am I."
print("isPalindrome("+input+"): " + str(isPalindrome(input)))
print("is_palindrome("+input+"): " + str(is_palindrome(input)))
