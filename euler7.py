#!/usr/bin/python
# Project Euler - Problem 7
# Author: Timothy Kinneen
# Version: 1.0.1
# ---------------------------------------------------------------------
# Description:
#  
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
# 
# What is the 10001st prime number?
#
# Answer: 104743 
# ---------------------------------------------------------------------

import time

# Checks every number between two and the passed value. If none divide
# evenly, function returns true 
def prime_checker(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = time.time()

# List will contain first 10001 prime numbers
prime_list = []

# Control variable
x = 2 
 
while x < 1000000:
    
    # If prime_checker returns true, current number is added to prime list 
    if prime_checker(x) == True:
        prime_list = prime_list + [x]

    # When the list has 10001 elements the script is done 
    if len(prime_list)  == 10001:
        print('The 10001st prime number is: ', prime_list[-1])
        
        # Calculates and outputs amount of time script took to run
        end = time.time()
        time_taken = end - start
        print()
        print('=================================')
        print('Script completed in {0:.2f} seconds.'.format(time_taken))
        exit()
        
    x = x + 1
