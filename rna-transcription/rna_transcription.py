def to_rna(dna_strand):
	strand = {
		'G' : 'C',
		'C' : 'G',
		'T' : 'A',
		'A' : 'U'
	}

	return ''.join([strand[dna] for dna in dna_strand])