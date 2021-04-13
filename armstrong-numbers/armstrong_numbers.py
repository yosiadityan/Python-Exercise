def is_armstrong_number(number):
	result = [int(digit)**len(str(number)) for digit in str(number)]
	return sum(result) == number