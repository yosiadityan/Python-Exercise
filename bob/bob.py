def is_question(string):
	return string.strip()[-1] == '?'

def is_yelling(string):
	check = [char.isupper() for char in string.strip() if char.isalpha()]
	if check == []:
		return False
	else:
		return all(check)

def calling(string):
	return [char for char in string.strip()] == []

def response(hey_bob):
	if calling(hey_bob):
		return "Fine. Be that way!"
	if is_question(hey_bob):
		if is_yelling(hey_bob):
			return "Calm down, I know what I'm doing!"
		else:
			return "Sure."
	else:
		if is_yelling(hey_bob):
			return "Whoa, chill out!"
		else:
			return "Whatever."