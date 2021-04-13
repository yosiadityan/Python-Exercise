import random
import string

class Robot:
	def __init__(self):
		self.name = Robot.nameGenerator()

	def reset(self):
		self.name = Robot.nameGenerator()

	@staticmethod
	def nameGenerator():
		random.seed()
		return ''.join(random.sample(string.ascii_uppercase, 2) + random.sample(string.digits, 3))