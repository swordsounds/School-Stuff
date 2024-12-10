# Generate two single-digit integers num1 and num2
# If num1 < num2, swap num1 with num2
# Ask the student to answer ’What is num1 - num2?
# Check the student’s answer and display whether the answer is correct
from random import *

# Generate two random integers
num1 = randint(0,9)
num2 = randint(0,9)


# Swap the numbers
if num1 < num2:
	temp_number = num1
	num1 = num2
	num2 = temp_number


answer = int(input("What is " + str(num1) + " - " + str(num2) + ":\n "))

result = num1 - num2

if answer == result:
	print("Correct! ", num1, "-", num2, "=", answer)
else:
	print("Incorrect", num1, "-", num2, "=", result)