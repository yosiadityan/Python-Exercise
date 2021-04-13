def slices(series, length):
	if length <= 0 or length > len(series):
		raise ValueError('Length is not matched')

	result = []
	for i in range(len(series)-length+1):
		result.append(series[i:i+length])
	return result