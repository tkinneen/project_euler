#!/usr/bin/python
# Project Euler - Problem 4 
# Author: Tim Kinneen
# Version: 1.0.1
# -----------------------------------------------------------------
# Description:
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 609906 
# -----------------------------------------------------------------

import time

start = time.time()

biggest = 0

# Below loops examine every number combination between 500 and 999, backwards 
for first in range(999, 500, -1):
    for second in range(998, 500, -1):
        
        # The product of the current loop iterations is calculated, then converted 
        # into a string 
        prod = first * second
        string = str(prod)
        
        # The below if statements compare digits within the product to find palindrome 
        if string[0] == string[5]:
            if string[1] == string[4]:
                if string[2] == string[3]:
                    
                    # Checks and collects the largest palindrome 
                    if prod > biggest:
                        biggest = prod

print("The largest palindrome that is a product of two numbers below 1000 is: ", biggest)

# Calculates and outputs amount of time script took to run
end = time.time()
time_taken = end - start
print()
print('=================================')
print('Script completed in {0:.2f} seconds.'.format(time_taken))
