def value(colors):
	color_band = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']

	value = 0
	for idx, color in enumerate(colors[1::-1]):
		value += color_band.index(color.capitalize()) * 10**idx
	return value