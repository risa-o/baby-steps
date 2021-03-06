# # Exercise 1: Write the code necessary to sum up all of the odd integers between 1 and 100. 
# You may use a previously defined function. 
# Hint: you'll likely need to produce a list of numbers..
def sum_odds():
	number = 0
	num_sum = 0
	num_list = []

	while number < 100:
		if number % 2 != 0:
			num_sum += number
		number += 1

	return num_sum
print(sum_odds())

#----------------------------------------------

# Exercise 2. Write a function called get_even_number that will only ever return an even number. 
# Inside the function, you may use the input() function to collect user input. 
# Hint: What's a good way to run code over and over based on a condition?
def enter_only_evens():
	num_entered = input("Please enter a number:  ")
	num_entered = int(num_entered)
	if num_entered % 2 == 0:
		return num_entered
	else:
		return(enter_only_evens())

#x = enter_only_evens()
#print(x)
#----------------------------------------------
# 3. Define a function named remove_item(list, value) that takes in two arguments. 
# The first argument should be an existing list and 
# the second argument should be a value you wish to remove from that list. Example: 
# bugs = ["mosquito", "ant", "scorpion", "ant", "ant", "mosquito", "typo", "type error"]
# remove_bugs("mosquito") returns ["scorpion", "ant", "ant", "typo", "type error"]

def remove_item(list_name,value):
	if value in list_name:
		list_name.remove(value)
		remove_item(list_name, value)
	return list_name

bugs = ["mosquito", "ant", "scorpion", "ant", "ant", "mosquito", "typo", "type error"]
#print(remove_item(bugs,"ant"))

#----------------------------------------------

# 4. Write a function named d20() that returns a random integer between 1 and 20, including both 1 and 20.
import random
def d20():
	return random.randint(1,20)

#print(d20())

#----------------------------------------------

# 5. Write a function named coin_toss that randomly returns a True or a False.
def coin_toss():
	return random.choice([True,False])	

#print(coin_toss())

#----------------------------------------------

# 6. Write a function named get_longest_string that takes in a list of strings and returns the longest string. Example: get_longest_string(["scorpion",
# "ant",
# "ant",
# "typo"]) returns "scorpion

def get_longest_string(list_name):
	return max(list_name, key = len)

print(get_longest_string(bugs))

#----------------------------------------------

# 7. Write a function named get_shortest_string that takes in a list of strings and returns the shortest string. Example: get_longest_string(["scorpion",
# "ant",
# "ant",
# "typo"]) returns "ant"

def get_shawty(list_name):
	return min(list_name, key = len)

print(get_shawty(bugs))
get_shortest_string = get_shawty
#----------------------------------------------

# 8. Write a function named first_to_last that takes in a sequence and 
# returns that sequence with the value at the first index moved to the last
#  index. Example: first_to_last([1, 2, 3]) returns [2, 3, 1].

def reverse_list(list_name):
	return list_name[::-1]

print(reverse_list(bugs))

#----------------------------------------------

# 9. Write a function named get_unique_values that takes in a sequence and 
# returns only the unique values in that sequence. Example: get_unique_values([1,
#  2, 2, 2, 2, 3, 3]) returns [1, 2, 3]. 

def get_unique_values(list_name):
	uniques = []
	for item in list_name:
		if item not in uniques:
			 uniques.append(item)
	return uniques

print (get_unique_values(bugs))

#----------------------------------------------

# 10. Write a function name frequencies that takes in a sequence and returns a dictionary 
# where each occuring value is a key and the corresponding value is the frequency count of that number 
# or character. 
# Example: frequencies("Bobby") returns {"B": 1, "o":1, "b":2, "y": 1}. 
# Example: frequencies(["mango", "guava", "mango", "kiwi"]) 
# returns {'mango': 2, 'guava': 1, 'kiwi': 1}. 
# Hint, the order of the keys does not matter since dictionaries, by definition, focus on the label for 
# ookup rather than the index to seek inside of iteration. 
# That means that frequencies(["mango", "guava", "mango", "kiwi"]) may just as well return 
# {'kiwi': 1, 'mango': 2, 'guava': 1} as well as {'guava': 1, 'kiwi': 1, 'mango': 2}.  

def frequencies(data):
	freq = {}
	for item in data:
		if item not in freq:
			freq[item] = 0
		freq[item] += 1	
	return freq

print(frequencies(bugs))