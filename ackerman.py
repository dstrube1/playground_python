#ackerman.py
#https://www.youtube.com/watch?v=i7sm9dzFtEI

def ack(m,n):
	if m == 0:
		return n+1
	elif n == 0:
		return ack(m-1,1)
	else:
		return ack(m-1, ack(m,n-1))

for m in range(5):
	for n in range(5):
		print("ack("+str(m)+","+str(n)+"): " + str(ack(m,n)))
