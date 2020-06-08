#challenge1

#input: integer
#output: list of prime factors

"""first attempt: almost good enough, 
but doesn't give list of all factors needed to get to the number
For example, with 630, returns list of [2,3,5,7]
should give list [2,3,3,5,7]

def get_prime_factors(input):
	if input < 2:
		return []
	primeList = []
	for x in range(2, input):
		if input % x == 0 and isPrime(x):
			primeList.append(x)
	if len(primeList) == 0:
		primeList.append(input)
	return primeList

def isPrime(candidate):
	for x in range(2, candidate):
		if candidate % x == 0 and x != candidate:
			return False
	return True
"""

def get_prime_factors(input):
	factors = list()
	divisor = 2
	while divisor <= input:
		if input % divisor == 0:
			factors.append(divisor)
			input = input/divisor
		else:
			divisor +=1
	return factors

input = 2
print("get_prime_factors("+str(input)+"): " + str(get_prime_factors(input)))
input = 15
print("get_prime_factors("+str(input)+"): " + str(get_prime_factors(input)))
input = 630
print("get_prime_factors("+str(input)+"): " + str(get_prime_factors(input)))
input = 13
print("get_prime_factors("+str(input)+"): " + str(get_prime_factors(input)))
input = 1
print("get_prime_factors("+str(input)+"): " + str(get_prime_factors(input)))
