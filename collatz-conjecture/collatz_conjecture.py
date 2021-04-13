def steps(number):
	if number <= 0:
		raise ValueError('Number must be positive')
	steps=0
	while number != 1:
		if number%2:
			number = 3*number+1
		else:
			number = number/2
		steps += 1
	return steps