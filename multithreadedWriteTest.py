#multithreadedWriteTest

#starting here:
#https://stackoverflow.com/questions/11983938/python-appending-to-same-file-from-multiple-threads

#Problem: How to print using multithreading
#Solution: Use 1 thread for printing

#Bug: There are 4 processing threads (0-3), but only thread 0 gets printed
#Next step: try with import multiprocessing

import queue  
import threading
import codecs
import multiprocessing

class PrintThread(threading.Thread):
	def __init__(self, ptQueue):
		threading.Thread.__init__(self)
		self.ptQueue = ptQueue

	def printFiles(self, queueOut): 
		print("PrintThread printing")
		print(queueOut, file=fileOut)

	def run(self):
		while True:
			queueOut = self.ptQueue.get()
			self.printFiles(queueOut)
			self.ptQueue.task_done()

class ComputeThread(threading.Thread):
	def __init__(self, in_queue, out_queue, index):
		threading.Thread.__init__(self)
		self.in_queue = in_queue
		self.out_queue = out_queue
		self.index = index

	def run(self):
		while True:
			path = self.in_queue.get()
			result = self.compute()
			self.out_queue.put(result)
			self.in_queue.task_done()

	def compute(self):
		print("ComputeThread computing thread #" + str(self.index))
		output = "index = " + str(self.index) + "; "
		for x in range(0, 100000):
			output = output + str(x) + " "
		return output

pathQueue = queue.Queue()
resultQueue = queue.Queue()

#https://docs.python.org/3/library/codecs.html
fileOut = codecs.open('file.txt', 'wt')
#https://docs.python.org/3/tutorial/inputoutput.html

# spawn threads to process
threadLimit = multiprocessing.cpu_count()

print("threadLimit: " + str(threadLimit))
for i in range(threadLimit):
	print("starting thread #" + str(i))
	t = ComputeThread(pathQueue, resultQueue, i)
	t.daemon = True
	t.start()

# spawn thread to print
t = PrintThread(resultQueue)
t.daemon = True
t.start()

pathQueue.put('.')

# wait for queue to get empty
pathQueue.join()
resultQueue.join()