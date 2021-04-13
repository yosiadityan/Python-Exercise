class SpaceAge:
	SPACE_AGE = {
		'Earth' : 365.25,
		'Mercury' : 0.2408467,
		'Venus' : 0.61519726,
		'Mars' : 1.8808158,
		'Jupiter' : 11.862615,
		'Saturn' : 29.447498,
		'Uranus' : 84.016846,
		'Neptune' : 164.79132
	}
	
	def __init__(self, seconds):
		self.seconds = seconds
		self.earth_age = seconds/(60*60*24*self.SPACE_AGE['Earth'])

	def on_earth(self):
		return round(self.earth_age, 2)

	def on_mercury(self):
		return round(self.earth_age/self.SPACE_AGE['Mercury'], 2)

	def on_venus(self):
		return round(self.earth_age/self.SPACE_AGE['Venus'], 2)

	def on_mars(self):
		return round(self.earth_age/self.SPACE_AGE['Mars'], 2)

	def on_saturn(self):
		return round(self.earth_age/self.SPACE_AGE['Saturn'], 2)

	def on_neptune(self):
		return round(self.earth_age/self.SPACE_AGE['Neptune'], 2)

	def on_uranus(self):
		return round(self.earth_age/self.SPACE_AGE['Uranus'], 2)

	def on_jupiter(self):
		return round(self.earth_age/self.SPACE_AGE['Jupiter'], 2)