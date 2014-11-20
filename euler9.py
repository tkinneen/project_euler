#!/usr/bin/python
# Project Euler - Problem 9
# Author: Tim Kinneen
# Version: 1.0.1
# -------------------------------------------------------------------
# Description:
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
#
#    a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.
#
# Answer: 31875000
# -------------------------------------------------------------------

import time

start = time.time()

# Nested loops cycle through all number combonations in the necessary range, 
#     checking them against our desired formulas
for x in range(1, 1000):
    for y in range(1, 1000):
        for z in range(1, 1000):

            # Proceeds if x squared added to y squared is equal to z squared 
            if (x * x) + (y * y) == (z * z):
                # If the three numbers added together equal 1000, we have a winner
                if x + y + z == 1000:
                    # The solution to this problem is the product of the three numbers found above
                    answer = x * y * z
                    print("Answer is: ", answer)
                    
                    # Calculates and outputs amount of time script took to run
                    end = time.time()
                    time_taken = end - start
                    print()
                    print('=================================')
                    print('Script completed in {0:.2f} seconds.'.format(time_taken))
                    exit()
