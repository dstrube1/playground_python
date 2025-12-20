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
# ===========================================================
# New
			if base == 10:
				if is_harshad_in_base_10(number):
					harshad_bases.append(base)
				# regardless of the result of is_harshad_in_base_10, 
				# skip to the next iteration of the loop, 
				# because we don't want to test base 10 twice
				continue
# END New
# ===========================================================
			if is_harshad_in_base(number, base):
				harshad_bases.append(base)
		print(f"\n{number} is a Harshad number in the following bases: {harshad_bases}" ) 
	except ValueError:
		print("Invalid input. Try again.")

# ===========================================================
# New stuff, i.e., mine
# at 1:02: "any number which is (evenly) divisible by the sum of its digits is a harshad number"
def get_digits_in_base_10(n):
	digits = list(str(n))
	# digits[::-1] <- this reverses the items in the list, but why?
	return digitis if digits else [0]

def digits_sum_in_base_10(n):
	# get list of characters in the number
	digits_str = get_digits_in_base_10(n)
	# convert the characters to integers
	digits = []
	for digit in digits_str:
		digits.append(int(digit))
	return sum(digits)

def is_harshad_in_base_10(n):
	print("base = 10, using is_harshad_in_base_10...")
	digit_sum = digits_sum_in_base_10(n)
	if digit_sum == 0:
		return False # avoid divide-by-zero
	# No remainder => evenly divisible
	return n % digit_sum == 0


# ===========================================================

if __name__ == "__main__":
	main()