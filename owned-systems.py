'''
Program: Mexen Games
Module: Owned Systems
Description: Get a list of all the systems owned by the user
Author: Danny Mexen
Version: 1
Date: 7th July 2021, Wednesday
Time: 22:52
'''

# Welcome message


def welcome_message():
	print('Please enter your name')
	name = input()
	return 'Welcome, ' + name + '!'

# Number of owned systems


def number_of_owned_systems():
	print('How many systems do you own?')
	number = input()
	return number

# List of owned systems


def list_of_owned_systems():
	number = int(number_of_owned_systems())
	all_systems = []
	for i in range(number):
		print('System ' + str(i + 1) + ' name: ')
		name = input()
		all_systems.append(name)
	return all_systems

# List of owned systems

# Main execution
# 1. Display welcome message
# 2. Ask for number of systems owned
# 3. Ask for list of systems owned
# 4. Display list of systems owned


extract_name = welcome_message()
name = extract_name[9:len(extract_name) - 1]
systems_list = list_of_owned_systems()
print(name + ', these are your systems.')
for i in range(len(systems_list)):
	print(str(i + 1) + '. ' + systems_list[i])
