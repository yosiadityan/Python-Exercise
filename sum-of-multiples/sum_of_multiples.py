def sum_of_multiples(limit, multiples):
	list_number = [_ for _ in range(1, limit) for div in multiples if div and not _%div]
	return sum(set(list_number))