#this function returns a list of every possible roll given a die of a given number of sides
def roll(sides):
	#initialize an empty list
	rolls = []
	#iterate from 0 to sides - 1
	for i in range(sides):
		#add each roll to the list
		rolls.append(i + 1)
	return rolls

#this function takes 2 lists of rolls, returns list of every possible roll when rolled with advantage
def advantage(base_rolls_1, base_rolls_2):
	#initialize empty list
	rolls = []
	#iterate through first list of rolls
	for base_roll_1 in base_rolls_1:
		#for every roll in the first list, iterate through all rolls in second list
		for base_roll_2 in base_rolls_2:
			#add the larger of the two to the rolls array
			if base_roll_1 > base_roll_2:
				rolls.append(base_roll_1)
			else:
				rolls.append(base_roll_2)
	return rolls

#like advantage, but reurns list of all disadvantage rolls
def disadvantage(base_rolls_1, base_rolls_2):
	#initialize empty list
	rolls = []
	#iterate through first list of rolls
	for base_roll_1 in base_rolls_1:
		#for every roll in the first list, iterate through all rolls in second list
		for base_roll_2 in base_rolls_2:
			#add the larger of the two to the rolls array
			if base_roll_1 < base_roll_2:
				rolls.append(base_roll_1)
			else:
				rolls.append(base_roll_2)
	return rolls

#given n dice rolls, return the highest
#this function takes a 2d list containing dice distributions
#every possible roll with the aforementioned rules is returned
def n_advantage(roll_distributions):
	#initialize empty list
	rolls = roll_distributions[0]
	#iterate through roll_distributions starting at roll_distributions[1]
	for i in range(len(roll_distributions) - 1):
		#set rolls to the advantage roll of itself with the next element of roll_distributions
		rolls = advantage(rolls, roll_distributions[i + 1])
	return rolls

#like n_advantage, but it takes the lowest roll instead
def n_disadvantage(roll_distributions):
	#initialize empty list
	rolls = roll_distributions[0]
	#iterate through roll_distributions starting at roll_distributions[1]
	for i in range(len(roll_distributions) - 1):
		#set rolls to the advantage roll of itself with the next element of roll_distributions
		rolls = disadvantage(rolls, roll_distributions[i + 1])
	return rolls
