class Allergies:

	def __init__(self, score):
		self.score = score
		self.allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

	def allergic_to(self, item):
		return item in self.lst

	@property
	def lst(self):
		return [ self.allergens[idx] for idx, val in enumerate(bin(self.score)[:-9:-1]) if val=='1' ]