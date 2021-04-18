def triplets_with_sum(number):
	all_sets = []
	# A set of pythagoras follow these rules:
	# - a < b < c
	# - a**2 + b**2 = c**2
	# While, we're looking for all sets of Pyth. that comply with this rule: a + b + c = Number
	# So, at min, a + b + c = a + a+1 + a+2 = Number
	# Which a = (Number-3)/3
	for a in range(1, int((number-3)/3)+1):
		for b in range(a+1, number):
			if number-(a+b) < b:
				continue
			else:
				c = number - a - b
				if a**2 + b**2 == c**2:
					all_sets.append([a, b, c])
	return all_sets