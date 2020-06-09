#challenge11
#https://www.linkedin.com/learning/python-code-challenges/generate-a-password?u=2163426

#Generate a password

#input: number of words in passphrase
#output: string of random words separated by spaces

#import random
#https://docs.python.org/3/library/random.html#module-random 
# : Warning: The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module.
# ->
#https://docs.python.org/3/library/secrets.html
import secrets

def generatePassphrase(num):
	sourceFile = "eff_large_wordlist.txt"
	#^: https://en.wikipedia.org/wiki/Diceware
	# -> https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
	with open(sourceFile, "rt") as file:
		lines = file.readlines() #[2:7778] #?
		wordlist = [line.split()[1] for line in lines]
	words = [secrets.choice(wordlist) for i in range(num)]
	return " ".join(words)

#since I didn't know enough to even attempt generatePassphrase, 
#I'm going ahead with a generatePassword func:
def generatePassword(length):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	num = "0123456789"
	special = "`~!@#$%^&*()-_=+[]\\{}|;':\",./<>?"
	allchars = alpha + alpha.upper() + num + special
	#print("special chars: ",special)
	#print("allchars: ", allchars)
	#print("password: ")
	password = ""
	for x in range(length):
		password += allchars[secrets.randbelow(len(allchars))]
	return password

#main
print(generatePassphrase(5))
print(generatePassword(20))

#https://docs.python.org/3/library/os.html#os.urandom
#print("random bytes?: ")
#import os
#print(os.urandom(4))