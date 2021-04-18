def primes(limit):
	if limit < 2:
		return []
	else:
		all_number = list(range(2, limit+1))
		for i in all_number:
			for x in range(i*2, limit+1, i):
				if x in all_number:
					all_number.remove(x)
		return all_number

# result = primes(13)
# print(result)