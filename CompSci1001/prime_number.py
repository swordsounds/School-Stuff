# Check if a number is a prime number
from math import *

# Obtain user input
num = int(input("Enter a number > 1 "))

# Sanity check
print("Square root of", num, "is", sqrt(num))

# Initializing our loop control variables
is_prime = True
divisor = 2

# While loop, 
# Checks if we have set is_prime to False
# Checks if our divisor is <= sqrt(num)
while is_prime and divisor <= sqrt(num):
	print("Checking if", num, "is divisble by", divisor)
	# If the remainder is 0,
	# Our number is not prime
	if num % divisor == 0:
		is_prime = False

	# Increment the divisor
	divisor = divisor + 1

# Print out output
if is_prime:
	print(num, "is a prime number")
else:
	print(num, "is not a prime number",
		"because it is divisible by", divisor-1)