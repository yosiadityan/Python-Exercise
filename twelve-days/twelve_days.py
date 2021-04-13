def recite(start_verse, end_verse):
	number = {
		12:	("twelfth", "twelve Drummers Drumming"),
		11: ("eleventh", "eleven Pipers Piping"),
		10: ("tenth", "ten Lords-a-Leaping"),
		9: ("ninth", "nine Ladies Dancing"),
		8: ("eighth", "eight Maids-a-Milking"),
		7: ("seventh", "seven Swans-a-Swimming"),
		6: ("sixth", "six Geese-a-Laying"),
		5: ("fifth", "five Gold Rings"),
		4: ("fourth", "four Calling Birds"),
		3: ("third", "three French Hens"),
		2: ("second", "two Turtle Doves"),
		1: ("first", "a Partridge in a Pear Tree")
	}

	if start_verse == end_verse:
		opening = [f"On the {number[start_verse][0]} day of Christmas my true love gave to me: "]
		main = []
		closing = ["a Partridge in a Pear Tree"]

		for i in range(start_verse, 1, -1):
			main.append(number[i][1] + ', ')
		if main != []:
			closing = ["and a Partridge in a Pear Tree"]

		lyric = [''.join(opening + main + closing + ['.'])]
	else:
		lyric = [''.join(recite(n,n)) for n in range(start_verse, end_verse+1)]

	return lyric