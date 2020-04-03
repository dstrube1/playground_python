#multithreadedWriteTest_0

import multiprocessing
import time
from queue import LifoQueue

def computeX(index,item,stackSize):
	_start = time.time()
	output = "index = " + str(index) + "; "
	for x in range(0, 10000000):
		pass
	resultQueue.put(output)
	print("Process {0} took {1} seconds to compute item {2} from stack which is now size: {3}".format(index, 
		(time.time() - _start), item, stackSize))

def printFromQueue():
	while True:
		queueOut = resultQueue.get()
		print(queueOut, file=fileOut)
		if resultQueue.empty():
			#this must be called before join_thread:
			resultQueue.close() 
			break

#https://docs.python.org/3/library/queue.html
#->
#https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue		
resultQueue = multiprocessing.Queue()

# max threads to process
cpu_count = multiprocessing.cpu_count()

processArray = []

#https://www.geeksforgeeks.org/stack-in-python/
stack = LifoQueue() 

for i in range(100):
	stack.put(i)

while not stack.empty():
	for index in range(cpu_count):
		if stack.empty():
			break
		item = stack.get()
		process = multiprocessing.Process(target=computeX, args=(index, item, stack.qsize(),))
		process.start()
		processArray.append(process)
	for j in range(cpu_count):
		processArray[j].join()

#https://docs.python.org/3/tutorial/inputoutput.html
#fileOut = open('file.txt', 'wt')
with open('file.txt', 'wt') as fileOut:
	printFromQueue()
#fileOut.close()
resultQueue.join_thread()