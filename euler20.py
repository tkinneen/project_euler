#!/usr/bin/python
# Project Euler - Problem 20 
# Author: Timothy Kinneen
# Version: 1.0.1
# -----------------------------------------------------------------
# Description: n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is:
#
#     3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!
#
# Answer: 648
# ---------------------------------------------------------------------------

import time

# Records the start time of the script
start = time.time()

# Records script end time, then calculates running time
end = time.time()
time_taken = end - start

# Variable declaration 
z = 100
prod = 0
sum = 0

# Loops through the n! sequence from 100 to 1
for x in range(1, 101):
    if z == 100:
        prod = z * 1
    else:
        prod = prod * z
    z = z - 1

# Converts the product to a string so each digit
#    can be iterated through
string_sum = str(prod)

# Loops through each digit, adding it to the running sum
for y in string_sum:
    # Each digit must be converted back to an integer
    y = int(y)
    sum = sum + y 

print('The answer is: ', sum)
    
# Outputs script run time
print()
print('=================================')
print('Script completed in {0:.2f} seconds.'.format(time_taken))
exit() 
