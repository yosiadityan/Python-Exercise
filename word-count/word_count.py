from collections import Counter
import re


def count_words(sentence):
	group = [re.sub('[:\.]', '', x) for x in re.split('[\s|,|_]', sentence.lower())]
	group_cleaned = [re.sub(r"[^\w\d\s\']+", '', x) for x in group]
	group_quote = [x.replace("'", "") if len(x)>=1 and (x[0]=="'" or x[-1]=="'") else x for x in group_cleaned]
	
	result = Counter(group_quote)
	
	try:
		result.pop('')
	except:
		pass
	
	return result