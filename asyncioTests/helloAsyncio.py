import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn())

"""
https://docs.python.org/3/library/asyncio.html
https://realpython.com/async-io-python/
https://www.geeksforgeeks.org/python/asyncio-in-python/
https://superfastpython.com/python-asyncio/
"""
