#challenge5
#https://www.linkedin.com/learning/python-code-challenges/play-the-waiting-game

#A pulse-pounding game of patience
#Player is prompted to wait a random amount of time between m & n seconds
import time
import random

def waitingGame():
	target = random.randint(2, 6)
	print("Your target time is " + str(target) + " seconds.")
	input("---Press Enter to Begin---")
	
	_start = time.perf_counter() 
	#.perf_counter() is higher accuracy than .time() for short durations
	print("Timer started. ")
	input("---Press Enter after "+str(target)+" seconds---")
	
	seconds = time.perf_counter() - _start
	print("You got {0:.3f} seconds".format(seconds))
	if seconds < target:
		print("{0:.3f} seconds too fast".format(target - seconds))
	elif target < seconds:
		print("{0:.3f} seconds too slow".format(seconds - target))
	else:
		print("WOW! Right on target")
waitingGame()