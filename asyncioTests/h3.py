import asyncio

"""
h3.py
was helloAsyncio, but was getting too big

see also h1
"""

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

# left off here:
# https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html#a-conceptual-overview-of-asyncio
# at "A homemade asyncio.sleep"

# See also :
# https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB

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
        "Beginning asynchronous sleep at time: " + 
        f"{datetime.datetime.now().strftime('%H:%M:%S')}."
    )
    
    await asyncio.create_task(async_sleep(3))
    
    print(
        "Done asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime('%H:%M:%S')}."
    )

    # asyncio.gather effectively awaits each task in the collection.
    await asyncio.gather(*work_tasks)

























