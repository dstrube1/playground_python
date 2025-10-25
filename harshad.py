# harshad.py
# from 9:29 in here:
# https://www.youtube.com/watch?v=dgwevhEykWQ

def get_digits_in_base(n, base):
	digits = []
	while n > 0:
		digits.append(n % base)
		n //= base
	return digits[::-1] if digits else [0]

def digits_sum_in_base(n, base):
	return sum(get_digits_in_base(n, base))

def is_harshad_in_base(n, base):
	digits_sum = digits_sum_in_base(n, base)
	if digit_sum == 0:
		return False # avoid divide-by-zero
	return n % digit_sum == 0

def main():
	try:
		number = int(input("Enter a positive integer: "))
		if number <= 0:
			print("Try again")
			return
		harshad_bases = []
		# print("\n{number}")
	except ValueError:
		print("Invalid input. Try again.")
if __name__ == "__main__":
	main()