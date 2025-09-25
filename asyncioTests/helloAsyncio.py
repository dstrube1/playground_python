import asyncio

"""
https://docs.python.org/3/library/asyncio.html
https://realpython.com/async-io-python/
https://www.geeksforgeeks.org/python/asyncio-in-python/
https://superfastpython.com/python-asyncio/
"""

async def hello():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

#asyncio.run(hello())

async def fn0():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

#asyncio.run(fn0())

#########################################################################################

# Similar to a coroutine function, calling a generator function does not run it. Instead, it creates a generator object.
# You can proceed to the next yield of a generator by using the built-in function next(). In other words, the generator runs, then pauses. For example:
def generatorExample():
	i = 0
	#This generator function will fail when called after the last yield
	#while i < 3:
	while True:
		i += 1
		yield i
	yield 0

def testGeneratorExample():
	j = 0
	generator = generatorExample()
	while j < 5:
		j += 1
		print("j = " + str(j) + "; i = " + str(next(generator)))

#testGeneratorExample()

#########################################################################################

# Since there’s only one event loop (in each thread), asyncio takes care of associating 
# the task with the event loop for you. As such, there’s no need to specify the event loop.

"""
# Warning-ful and erroneous code bits:

async def coroutineFunction(number: int):
    print( f"number is: {number}." )
    await asyncio.sleep(1)

coroutineObject = coroutineFunction(number=5)

# This creates an event loop and indefinitely cycles through
# its collection of jobs.
#event_loop = asyncio.new_event_loop()
#event_loop.run_forever()

# This creates a Task object and schedules its execution via the event loop.
#task = asyncio.create_task(coroutineObject)
#asyncio.run(coroutineObject)
"""

# The task itself is not added to the event loop, only a callback to the task is. This 
# matters if the task object you created is garbage collected before it’s called by the event loop

#########################################################################################

async def coroutine_a(taskOrCoroutine):
   print("a: " + taskOrCoroutine)

async def coroutine_b():
   print("bbb")

async def taskCoroutineExample():
	# Unlike tasks, awaiting a coroutine does not hand control back to the event loop!
	task_b = asyncio.create_task(coroutine_b())
	num_repeats = 3
	for _ in range(num_repeats):
   		#If just coroutines, execute first; if just tasks, last; if mix, it's a mix
		await coroutine_a("coroutine")
		await asyncio.create_task(coroutine_a("task"))
	await task_b
	#Using only await coroutine could unintentionally hog control from other tasks and effectively stall the event loop

# asyncio.run(taskCoroutineExample())

#########################################################################################

class Rock:
    def __await__(self):
        value_sent_in = yield 7
        print(f"Rock.__await__ resuming with value: {value_sent_in}.")
        return value_sent_in

async def CSE(): # Coroutine Send Example
    print("Beginning coroutine CSE().")
    rock = Rock()
    print("Awaiting rock...")
    # await calls the __await__() method of the given object
    value_from_rock = await rock
    print(f"Coroutine received value: {value_from_rock} from rock.")
    return 23

coroutine = CSE()
intermediate_result = coroutine.send(None)
print(f"Coroutine paused and returned intermediate value: {intermediate_result}.")

print(f"Resuming coroutine and sending in value: 42.")
try:
	coroutine.send(42)
except StopIteration as e:
	print("Caught StopIteration")
	# When a coroutine finishes, it raises a StopIteration exception with the return value attached in the value attribute
	returned_value = e.value
print(f"Coroutine CSE() finished and provided value: {returned_value}.")

# Output:
"""
Beginning coroutine CSE().
Awaiting rock...
Coroutine paused and returned intermediate value: 7.
Resuming coroutine and sending in value: 42.
Rock.__await__ resuming with value: 42.
Coroutine received value: 42 from rock.
Caught StopIteration
Coroutine CSE() finished and provided value: 23.
"""

#########################################################################################

async def other_work():
    print("I like work. Work work work.")

async def main():
    # Add a few other tasks to the event loop, so there's something
    # to do while asynchronously sleeping.
    work_tasks = [
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work())
    ]
    print(
        "Beginning asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    await asyncio.create_task(async_sleep(3))
    print(
        "Done asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    # asyncio.gather effectively awaits each task in the collection.
    await asyncio.gather(*work_tasks)

# left off here:
# https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html#a-conceptual-overview-of-asyncio
# at "A homemade asyncio.sleep"

























