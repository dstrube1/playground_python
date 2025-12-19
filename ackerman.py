#ackerman.py
#https://www.youtube.com/watch?v=i7sm9dzFtEI

import sys

def ack(m,n,level):
	if m == 0:
		return n+1
	elif n == 0:
		level += 1
		return ack(m-1,1,level)
	else:
		#print("return ack(m-1, ack(m,n-1,level),...) => ack(" + str(m) + "-1, ack(" + str(m) + "," + str(n) + "-1," + str(level) + ")")
		level += 1
		return ack(m-1, ack(m,n-1,level),level)
for m in range(5):
	for n in range(5):
		try:
			print("ack(" + str(m) + "," + str(n) + "): " + str(ack(m,n,0)))
		except RecursionError as rerr:
			# Generic error
			#print("Caught RecursionError:" + str(rerr))
			# Specific error
			print("Caught RecursionError - exceeded recursion limit: " + str(sys.getrecursionlimit()))
			
			break
		except:
			print("Caught some unexpected error")
