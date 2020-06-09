#challenge9
#https://www.linkedin.com/learning/python-code-challenges/simulate-dice?u=2163426

#Simulate dice
#function to determine the probability of certain outcomes when rolling dice
#assume d6

#Using Monte Carlo Method: Trial 1 - 1,000,000
#Roll dice over and over, see how many times each occurs, calculate probability from that

import random

#input: variable number of arguments for sides of dice
#output: table of probability for each outcome
def diceRoll(numSides):
	counts = []
	for x in range(1, numSides+1):
		counts.append(0)
		#print("x: " + str(x))
	maxRolls = 1_000_000 #neat trick to make big numbers more human readable
	for x in range(maxRolls):
		dice = random.randint(1, numSides)
		counts[dice-1] += 1
	print("results:")
	for x in range(numSides):
		print(str(x+1) + " probability: {:0.2f}% chance ".format((counts[x] / maxRolls) * 100) )

#instructor's solution- I underestimated what he meant by the input & output
from collections import Counter
def roll_dice(*dice, num_trials=1_000_000):
	counts = Counter()
	for roll in range(num_trials):
		counts[sum((random.randint(1, sides) for sides in dice))] += 1
	print("\nOutcome\tProbability")
	for outcome in range(len(dice), sum(dice)+1):
		print("{}\t{:0.2f}%".format(outcome, counts[outcome]*100/num_trials))

#main
diceRoll(10)

roll_dice(4,6,6)
#ok, compactified logic aside, that is pretty cool