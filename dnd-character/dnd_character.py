import random

class Character:
	@staticmethod
	def ability():
		dice = [random.randint(1,6) for x in range(4)]
		return sum(dice) - min(dice)

	def __init__(self):
		self.strength = Character.ability()
		self.dexterity = Character.ability()
		self.constitution = Character.ability()
		self.intelligence = Character.ability()
		self.wisdom = Character.ability()
		self.charisma = Character.ability()
		self.hitpoints = 10+modifier(self.constitution)

def modifier(number):
	return (number-10)//2