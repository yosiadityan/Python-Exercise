from collections import Counter

def find_anagrams(word, candidates):
	expected = []
	count_word = Counter(word.lower())
	for c in candidates:
		if word.lower() != c.lower() and count_word == Counter(c.lower()):
			expected.append(c)
	return expected