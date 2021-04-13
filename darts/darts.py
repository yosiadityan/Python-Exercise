def score(x, y):
	point = x**2 + y**2
	if point > 10**2:
		return 0
	elif point > 5**2 :
		return 1
	elif point > 1**2 :
		return 5
	else:
		return 10