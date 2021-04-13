"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'

from collections import Counter

def score(dice, category):
	dice_counter = Counter(dice)
	global_var = globals().copy()

	# Yacht
	if len(set(dice)) == 1:
		global_var[YACHT] = 50
	
	# Choice
	global_var[CHOICE] = sum(dice)

	# Big Straight
	if set(dice) == {2, 3, 4, 5, 6}:
		global_var[BIG_STRAIGHT] = 30

	# Little Straight
	if set(dice) == {2, 3, 4, 5, 1}:
		global_var[LITTLE_STRAIGHT] = 30

	# Four of a kind, Ones, Twos, Threes, Fours, Fives, Sixes
	for k, v in dice_counter.items():
		if v>=4:
			global_var[FOUR_OF_A_KIND] = k*4

		if k==1:
			global_var[ONES] = k*v
		if k==2:
			global_var[TWOS] = k*v
		if k==3:
			global_var[THREES] = k*v
		if k==4:
			global_var[FOURS] = k*v
		if k==5:
			global_var[FIVES] = k*v
		if k==6:
			global_var[SIXES] = k*v

	# Full House
	if set(dice_counter.values()) == {2, 3}:
		global_var[FULL_HOUSE] = sum(dice)

	# Return value
	if isinstance(global_var[category], str):
		return 0
	else:
		return global_var[category]