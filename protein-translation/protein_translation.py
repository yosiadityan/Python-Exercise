def proteins(strand):
	codon = {
		'Methionine' 	: ['AUG'],
		'Phenylalanine' : ['UUU', 'UUC'],
		'Leucine' 		: ['UUA', 'UUG'],
		'Serine' 		: ['UCU', 'UCC', 'UCA', 'UCG'],
		'Tyrosine' 		: ['UAU', 'UAC'],
		'Cysteine' 		: ['UGU', 'UGC'],
		'Tryptophan' 	: ['UGG']
	}

	result = []
	observed = strand[:3]
	i = 0
	while observed not in 'UAA, UAG, UGA'.split(', ') and i<len(strand):
		for key, val in codon.items():
			if observed in val:
				result.append(key)
		i += 3
		observed = strand[i:i+3]
	return result