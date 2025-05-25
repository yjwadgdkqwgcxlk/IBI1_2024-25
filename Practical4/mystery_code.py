# What does this piece of code do?
# Answer:This code simulates rolling two dice repeatedly until a pair of matching numbers is rolled, and tracks the number of rolls it takes.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0   #"progress"means the number of times the dices are throwm to make the numbers on the two dices the same.
while progress>=0:
	progress+=1
	first_n = randint(1,6) # to get the number on the first dice
	second_n = randint(1,6)  # to get the number on the second dice
	if first_n == second_n:
		print(progress)
		break



