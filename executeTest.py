import time

call_count = 0

def execute_with_retry(operation, max_attempts=5, base_delay=0.5):
	fatal = (ValueError, TypeError)
	transient = (ConnectionError, TimeoutError)
	
	attempt = 0
	last_error = None
	delay = base_delay
	
	while attempt < max_attempts:
		try:
			result = operation()
		except fatal:
			raise
		except transient as e:
			last_error = e
			attempt += 1
			time.sleep(delay)
			delay = min(delay * 2, 10.0)
			continue
		except Exception as e:
			last_error = e
			attempt += 1
			time.sleep(base_delay)
			continue
		if result is None and attempt < max_attempts - 1:
			attempt += 1
			time.sleep(delay)
			delay *= 2
			continue
		return result
	raise RuntimeError(f"Failed after {attempt} attempts") from last_error

"""
Suppose operation() behaves as follows on successive calls:
1: Raises ConnectionError
2: Raises TimeoutError
3: Returns None
4: Raises Exception("boom")
5: Returns "success"

Using the default parameters of execute_with_retry, what is the total amount of time slept (in seconds), and what value does the function return?

A: Total sleep time: 4.0 seconds; Return value: "success"
B: Total sleep time: 7.5 seconds; Return value: "success"
C: Total sleep time: 4.0 seconds; function raises RuntimeError
D: Total sleep time: 3.5 seconds; Return value: "success"

Answer: A
"""

def op():
	global call_count
	call_count += 1
	if call_count == 0:
		print("Invalid value")
		return
	if call_count == 1:
		raise ConnectionError("ConnectionError")
	elif call_count == 2:
		raise TimeoutError("TimeoutError")
	elif call_count == 3:
		return None
	elif call_count == 4:
		raise Exception("boom")
	elif call_count == 5:
		return "success"
	else:
		print("Invalid value")
		return

def getTime(seconds):
	#from https://github.com/dstrube1/CS7641/blob/main/assignments/A2/submission
	if int(seconds / 60) == 0:
		return str(int(seconds)) + " second(s)"
	minutes = int(seconds / 60)
	seconds = int(seconds % 60)
	if int(minutes / 60) == 0:
		return str(minutes) + " minute(s) and " + str(seconds) + " second(s)"
	hours = int(minutes / 60)
	minutes = int(minutes % 60)
	# Assuming this won't be called for any time span greater than 24 hours
	return str(hours) + " hour(s), " + str(minutes) + " minute(s), and " + str(seconds) + " second(s)"

def main():
	start = time.time()
	result = execute_with_retry(op)
	end = time.time()
	print(f"Result: {result} in {getTime(end - start)}")


if __name__ == "__main__":
	main()