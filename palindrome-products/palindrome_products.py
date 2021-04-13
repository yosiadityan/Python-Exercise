def is_palindrome(number):
	return str(number) == str(number)[::-1]


def factor(min_factor, max_factor, product):
	result = []
	for i in range(min_factor, max_factor+1):
		for j in range(min_factor, i+1):
			if i*j == product:
				result.append([j, i])
	return result


def palindrome_product(min_factor, max_factor, which='min'):
	if min_factor > max_factor:
		raise ValueError('Exception')

	product = []
	for i in range(min_factor, max_factor+1):
		for j in range(min_factor, i+1):
			if is_palindrome(i*j):
				product.append(i*j)
	if which == 'min':
		return min(product, default=None)
	else:
		return max(product, default=None)


def largest(min_factor, max_factor):
	product = palindrome_product(min_factor, max_factor, which='max')
	return product, factor(min_factor, max_factor, product)


def smallest(min_factor, max_factor):
	product = palindrome_product(min_factor, max_factor, which='min')
	return product, factor(min_factor, max_factor, product)