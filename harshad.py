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
	digit_sum = digits_sum_in_base(n, base)
	if digit_sum == 0:
		return False # avoid divide-by-zero
	return n % digit_sum == 0

def main():
	try:
		number = int(input("Enter a positive integer: "))
		# 2016502858579884466176 ?
		if number <= 0:
			print("Try again")
			return
		harshad_bases = []
		for base in range(2,21):
			if is_harshad_in_base(number, base):
				harshad_bases.append(base)
		print(f"\n{number} is a Harshad number in the following bases: {harshad_bases}" ) 
	except ValueError:
		print("Invalid input. Try again.")
if __name__ == "__main__":
	main()