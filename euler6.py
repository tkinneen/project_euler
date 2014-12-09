#!/usr/bin/python
# Project Euler - Problem 6 
# Author: Timothy Kinneen
# Version: 1.0.1
# -----------------------------------------------------------------
# Description: The sum of the squares of the first ten natural numbers is:
#
#    12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is:
#
#    (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 − 385 = 26.
#
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
#
# Answer: 55164150
# ---------------------------------------------------------------------------

import time

# Records the start time of the screipt 
start = time.time()

sum_of_squares = 0
sum_of_naturals = 0

# Loops through all natural numbers between 1 and 100 
for x in range(1, 101):

    # Adds each new number to the running sum 
    sum_of_naturals = sum_of_naturals + x

    # Calculates the square of the current iteration, then adds it to the sum  
    sq = x * x
    sum_of_squares = sum_of_squares + sq

temp = sum_of_naturals * sum_of_naturals

# Calculates and outputs the differnce 
difference = temp - sum_of_squares

print("Answer: ", difference)

# Records script end time, then calculates running time
end = time.time()
time_taken = end - start

# Outputs script run time
print()
print('=================================')
print('Script completed in {0:.2f} seconds.'.format(time_taken))
