#mwPrime.py
#Author: David Strube
#Date: 2021-12-19
#What is: Having a go at searching for the most wanted prime 
"""
Most wanted prime:
https://www.youtube.com/watch?v=vKlVNFOHJ9I

Confirmed ns: 10, 2446

Search has gone up to 1 million (1000000)

Let's look up to 2 million. If that does get unreasonable, go higher

Searching in Java with BigInteger was taking a while, using isProbablePrime
Let's try with this:
https://en.wikipedia.org/wiki/Primality_test#Python

"""

"""	
This is not all that fast for n = 10
def is_prime(n: int) -> bool:
	#""Primality test using 6k+-1 optimization.""
	if n <= 3:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i ** 2 <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True
"""

"""x"""
#Let's try something else: 
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
#No, this gets even slower at n = 5

def is_in_Sieve(test: int) -> bool:
	# Create a boolean array "prime[0..n]" and initialize
	# all entries it as true. A value in prime[i] will
	# finally be false if i is Not a prime, else true.
	prime = [True for i in range(test + 1)]
	p = 2
	while (p * p <= test):
		# If prime[p] is not changed, then it is a prime
		if (prime[p] == True):
			# Update all multiples of p
			for i in range(p ** 2, test + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	#for p in range(test + 1):
	#	if prime[p]:
	#		return True #print p, #Use print(p) for python 3
	return prime[test]
"""x"""

if __name__ == "__main__":
	#for n in range(2, 12):
	#n = 2
	digits = "123454321"
	#for i in range(1,n+1):
	#	digits += str(i)
	#for i in reversed(range(1,n)):
	#	digits += str(i)
	
		#print("Digits: " + digits)
	print("n: " + str(5) + " - is prime?: " + str(is_in_Sieve(int(digits))))































