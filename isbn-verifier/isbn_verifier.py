def is_valid(isbn):
	chars = [x for x in isbn if x.isalnum()]

	if chars == [] or len(chars)!=10 or not all(list(map(str.isdigit, chars[:-1]))):
		return False

	if chars[-1] == 'X':
		chars[-1] = '10'
	elif not chars[-1].isdigit():
		return False

	value = list(map(lambda x: x[0]*int(x[1]), zip(range(10,0,-1), chars)))
	return not sum(value)%11