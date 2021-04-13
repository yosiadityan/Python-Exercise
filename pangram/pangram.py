import string

def is_pangram(sentence):
    word_list = {word for word in sentence.lower().strip() if word.isalnum() and word.isalpha()}
    return set(string.ascii_lowercase) == word_list