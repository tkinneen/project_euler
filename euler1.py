#!/usr/bin/python
# Project Euler - Problem 1
# Author: Timothy Kinneen
# Version: 1.0.1
# -----------------------------------------------------------------
# Description:
#
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168
# ------------------------------------------------------------------

import time

# Records the time the script starts running  
start = time.time()

# This variable will contain the sum of all applicable multiples 
mult_sum = 0

# Loops through the first 1000 numbers.  If the current number is
# divisible by 3 or 5, it gets added to the running sum
for x in range(1, 1000):
    if x % 3 == 0:
        mult_sum = mult_sum + x
    elif x % 5 == 0:
        mult_sum = mult_sum + x

# Once the loop has run, the answer is output
print()
print('Sum of all mutiples of 3 and 5 that are below 1000:', mult_sum)

# Records script end time, then calculates running time
end = time.time()
time_taken = end - start

# Outputs script run time
print()
print('=================================')
print('Script completed in {0:.2f} seconds.'.format(time_taken))
        
    

