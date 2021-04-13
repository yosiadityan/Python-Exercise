def classify(number):
	if number <= 0:
		raise ValueError('Number must be positive')
	else:
		factor = [x for x in range(1, number//2+1) if not number%x]

	if sum(factor) < number:
		return 'deficient'
	elif sum(factor) == number:
		return 'perfect'
	else:
		return 'abundant'