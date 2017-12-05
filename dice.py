
from random import randint

class Dice:
	def __init__(self, value):
		self.value = value

	def roll(self):
		return randint(1,6)
