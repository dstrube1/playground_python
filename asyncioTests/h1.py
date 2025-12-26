import asyncio

"""
h1.py
was helloAsyncio, but was getting too big

https://docs.python.org/3/library/asyncio.html
https://realpython.com/async-io-python/
https://www.geeksforgeeks.org/python/asyncio-in-python/
https://superfastpython.com/python-asyncio/
"""

async def hello():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(hello())

async def fn0():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn0())

#########################################################################################

# Similar to a coroutine function, calling a generator function does not run it. Instead, it creates a generator object.
# You can proceed to the next yield of a generator by using the built-in function next(). In other words, the generator runs, then pauses. For example:
def generatorExample():
	i = 0
	#This generator function will fail when called after the last yield; throws a StopIteration
	while i < 3:
	#while True:
		i += 1
		yield i
	yield 0

def testGeneratorExample():
	j = 0
	generator = generatorExample()
	while j < 5:
		j += 1
		try:
			print("j = " + str(j) + "; i = " + str(next(generator)))
		except StopIteration as si:
			print("Caught StopIteration exception: " + str(si)) #no content
testGeneratorExample()
























