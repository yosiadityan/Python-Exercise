from collections import Counter

def is_isogram(string):
	new_str = [char for char in string.lower() if char.isalnum()]
	letter_count = Counter(new_str)
	return all([count == 1 for count in letter_count.values()])