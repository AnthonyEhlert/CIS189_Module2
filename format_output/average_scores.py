"""
Program: average_scores.py
Author: Tony Ehlert
Last date modified: 1/18/2023

The purpose of this program is accept user input to display a formatted string
   representing a user's first name, last name, age, and average score
The input is a user's first name, last name, and age. As well as three scores for the user
The output is a string displaying the user's last name, first name, age, and average score
"""

#import constants.py for constant variables
import constants

# prompt user for first name and store it in first_name variable
first_name = input("Please enter your first name: ")

# use capitalize() method to format first name
first_name = first_name.capitalize()

# prompt user for last name and store it in first_name variable
last_name = input("Please enter your last name: ")

# use capitalize() method to format last name
last_name = last_name.capitalize()

# test print line to verify name variables start with upper case characters
#print(last_name + " " + first_name)

# prompt user for their age & store it in user_age_as_int variable (input cast to int)
user_age = input("Please enter your age: ")

# cast input to float type to handle incorrect entry
user_age_as_float = float(user_age)

# cast to int type for future manipulations
user_age_as_int = int(user_age_as_float)

# test print line to validate that user_age_as_int was cast as int
# print(user_age_as_int + 1)

# prompt user for their three scores (cast to int) & assign to variables
score_one_as_int = int(input("Please enter your first score: "))
score_two_as_int = int(input("Please enter your second score: "))
score_three_as_int = int(input("Please enter your third score: "))

# calculate total score and assign to variable
scores_total = score_one_as_int + score_two_as_int + score_three_as_int

# test to verify scores_total is correct
# print(scores_total)

# calculate average score and assign to variable
avg_score = scores_total / constants.NUM_OF_SCORES

# test to verify avg_score was calculated correctly
# print(avg_score)

# creation of output string and assigning to variable
output_string = f"{last_name}, {first_name} age: {user_age_as_int: 3d} average grade: {avg_score: 5.2f}"

# print out of final output_string
print(output_string)

# observed outputs after manually running code
# Test 1, TONY eHLERT 36 100 100 100 = "Ehlert, Tony age:  36 average grade:  100.00"
# Test 2, jane doe 33 95 100 105 = "Doe, Jane age:  33 average grade:  100.00"
# Test 3, John Smith 25 70 80 90 = "Smith, John age:  25 average grade:  80.00"
# Test 4, jIM BoB 100.25 65 80 90 = "Bob, Jim age:  100 average grade:  78.33"


