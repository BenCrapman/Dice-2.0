#developed by ben chapman

import math

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

#given a dice distribution, gives the percent probability of each roll happening
#the value of the roll is represented by the index (0 should always be 0%)
#the probability distribution is returned as a list
def roll_distribution(roll):
	#initialize distribution as empty list
	distribution = []
	max_roll = 0
	num_possibilities = len(roll)
	#finds highest number in the distribution
	for i in roll:
		if i > max_roll:
			max_roll = i
	#gives distribution max_roll + 1 elements, all starting at 0
	for i in range(max_roll + 1):
		distribution.append(0)
	#add 1 to the corresponding roll in distribution for every time that roll shows up
	for i in roll:
		distribution[i] += 1
	#typecast every element to float, multiply by 100, divide by the number of possible rolls
	for i in range(len(distribution)):
		distribution[i] *= 100.0
		distribution[i] /= num_possibilities
	return distribution

#given a percent-based distribution of rolls (like those recieved from roll_distribution), return average roll
def distribution_average(distribution):
	mu = 0.0
	#add roll value * p of happening for every possible roll
	for i in range(len(distribution)):
		mu += distribution[i] * i
	mu /= 100.0
	return mu

#given an average roll and a percent-based distribution of rolls, return standard deviation
def distribution_standard_deviation(mu, distribution):
	sigma = 0.0
	#add magnitude of difference between average and measured value
	for i in range(len(distribution)):
		sigma += math.fabs((distribution[i] * i / 100.0) - mu)
	#divide by total number of values to get the average difference in values from the average value
	sigma /= len(distribution)
	return sigma

#function used for testing, non-permanent
def test():
	#define variables
	rolls = [roll(20), roll(20), roll(20), roll(20)]
	roll_data = n_advantage(rolls)
	distribution = roll_distribution(roll_data)
	average = distribution_average(distribution)
	standard_deviation = distribution_standard_deviation(average, distribution)
	#print out results
	print 'average roll: ' + str(average)
	print 'standard deviation: ' + str(standard_deviation)

def user_roll():
	#initialize variables
	rolls = []
	num_rolls = 0
	roll_type = ''
	num_sides = 20
	roll_data = []
	distribution = []
	print_distribution = False
	average = 0
	standard_deviation = 0
	#get user input
	print 'Roll Statistics Calculator'
	num_sides = int(raw_input('number of sides: '))
	num_rolls = int(raw_input('number of dice: '))
	print_distribution = (raw_input('type "yes" if you want the entire distribution: ') == 'yes')
	if num_rolls > 1:
		#asks whether roll is with advantage or disadvantage, unless there's only one dice rolled
		while (roll_type != 'advantage') and (roll_type != 'disadvantage'):
			roll_type = raw_input('advantage or disadvantage? (must be one or the other): ')
		#populates rolls with n dice rolls
		for i in range(num_rolls):
			rolls.append(roll(num_sides))
		#condenses data in rolls down into one roll with advantage or disadvantage
		if roll_type == 'advantage':
			roll_data = n_advantage(rolls)
		else:
			roll_data = n_disadvantage(rolls)
	else:
		#if there's only one die rolled, roll_data is just filled with a single roll
		roll_data = roll(num_sides)
	#distribution data is calculated
	distribution = roll_distribution(roll_data)
	average = distribution_average(distribution)
	standard_deviation = distribution_standard_deviation(average, distribution)
	#data is displayed
	if print_distribution:
		#adds a number of spaces between the roll and it's frequency
		#this makes it look neater
		for i in range(len(distribution)):
			colon = ':'
			for j in range(4 - len(str(i))):
				colon += ' '
			print str(i) + colon + str(distribution[i]) + '%'
	print 'average roll: ' + str(average)
	print 'standard deviation: ' + str(standard_deviation)
		
				

user_roll()
