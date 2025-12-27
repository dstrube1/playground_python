import asyncio

"""
h2.py
was helloAsyncio, but was getting too big

see also h1
"""

# Since there’s only one event loop (in each thread), asyncio takes care of associating 
# the task with the event loop for you. As such, there’s no need to specify the event loop.

async def coroutineFunction(number: int):
    print( f"number is: {number}." )
    await asyncio.sleep(1)

coroutineObject = coroutineFunction(number=1)
# This creates a Task object and schedules its execution via the event loop.
asyncio.run(coroutineObject)

# This creates an event loop :
event_loop = asyncio.new_event_loop()

# This indefinitely cycles through its collection of jobs:
#event_loop.run_forever()

try:
	# RuntimeError: no running event loop
	task = asyncio.create_task(coroutineObject)
	# This is because asyncio.create_task() schedules a coroutine on the currently running event loop.
	# But when Python is just importing or running the script normally, no event loop is running yet,
	# so asyncio.create_task() fails.
except RuntimeError as rerr:
	print("Caught RuntimeError: " + str(rerr))
# Solution 1 — Wrap everything in an async function and call via asyncio.run():
async def main(coroutineFunctionParam):
	task = asyncio.create_task(coroutineFunction(coroutineFunctionParam))
	await task
asyncio.run(main(2))
# Solution 2 - If you really need to schedule from top level, explicitly get/create a loop
# (Not recommended for most modern asyncio code.)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(coroutineFunction(3))
loop.run_until_complete(task)

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
	# Using only await coroutine could unintentionally hog control from other tasks and effectively stall the event loop

asyncio.run(taskCoroutineExample())
























