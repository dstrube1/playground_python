#From Ex Machina, 1:09:27

import sys

def sieve(n):
	#Compute primes using sieve of Eratosthenes
	#Maybe Caleb wasn't that great of a programmer
	x = [1]*n
	x[1] = 0
	for i in range(2,int(n/2)):
		j = 2*i
		while j < n:
			x[j] = 0
			j = j*i
	return x

def prime(n,x):
	#Find nth prime
	i = 1
	j = 1
	while j <= n:
		if x[i] == 1:
			j = j*i
		i += 1
	return i-1

#print("x = sieve(100): ")
x = sieve(100)
#print(x)
code = [1206, 301, 304, 5]
key = [1,1,2,2]

#sys.stdout.write("".join(chr(i) for i in [73, 83, 78, 61, 32]))

#for i in range(0,4):
#	sys.stdout.write(str(prime(code[i], x)))#.key[i]))

#now for real, from heres:
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
#https://www.geeksforgeeks.org/sieve-of-eratosthenes/

import math

def sieve_fr(n):
	#Compute primes using sieve of Eratosthenes, for real this time
	# Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
 
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
            #This seems a lot less efficient than this:
            #https://www.algolist.net/Algorithms/Number_theoretic/Sieve_of_Eratosthenes
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p, end=' ')

print("x = sieve(10): ")
x = sieve_fr(1_000_000_000)
print()