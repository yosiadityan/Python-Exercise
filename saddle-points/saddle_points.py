def saddle_points(matrix):
	if matrix == []:
		return []
	elif len(set([len(row) for row in matrix])) > 1:
		raise ValueError("Irregular Matrix")

	row = len(matrix)
	col = len(matrix[0])
	result = []

	for i in range(row):
		for j in range(col):
			entire_row = matrix[i]
			entire_col = [matrix[_][j] for _ in range(row)]

			if matrix[i][j] == max(entire_row) and matrix[i][j] == min(entire_col):
				result.append({"row": i+1, "column": j+1})

	return(result)