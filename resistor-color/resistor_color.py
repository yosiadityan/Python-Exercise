def color_code(color):
	return colors().index(color)


def colors():
	return list(map(str.lower, ['Black','Brown','Red','Orange','Yellow','Green',\
								'Blue','Violet','Grey','White']))