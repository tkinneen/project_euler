#!/usr/bin/python
# Project Euler - Problem 5
# Author: Tim Kinneen 
# Version: 1.0.1 
# ---------------------------------------------------------------
# Description:  
# 
# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?
# 
# Answer: 232792560 
# ----------------------------------------------------------------

import time

# Records script's start time
start = time.time()

# Starts on number where description leaves off
num = 2520

# Checks each number for divisibility of first 20 numerals. To decrease processing time, 
# certain numbers can be omitted because a previous number's divisibility makes it redundant 
while True:
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                if num % 7 == 0:
                    if num % 11 == 0:
                        if num % 13 == 0:
                            if num % 16 == 0:
                                if num % 17 == 0:
                                    if num % 18 == 0:
                                        if num % 19 == 0:
                                            if num % 20 == 0:
                                                print('Correct answer is: ', num)
                                    
                                                # Calculates and outputs script running time 
                                                end = time.time()
                                                final = end - start
                                                print()
                                                print('---------------------------')
                                                print("Script ran in {0:.2f} seconds".format(final))
                                                exit()
    
    # If current number is not divisible, increase by 1 and loop again
    num = num + 1



