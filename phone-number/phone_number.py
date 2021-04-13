import re

class PhoneNumber:
	def __init__(self, number):
		digits = [x for x in number if x.isalnum()]
		if len(digits) < 10:
			raise ValueError('Phone number is not correct')
		elif len(digits) > 10:
			if digits[0] != '1':
				raise ValueError('Phone number is not correct')
			else:
				digits.pop(0)

		if (digits[0] in '01' or digits[3] in '01'):
			raise ValueError('Phone number is not correct')

		self.number = ''.join(digits)
		self.area_code = self.number[:3]

	def pretty(self):
		return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'