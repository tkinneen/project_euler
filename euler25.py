#!/usr/bin/python
# Project Euler - Problem 25 
# Author: Timothy Kinneen
# Version: 1.0.1
# -----------------------------------------------------------------
# Description: The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#   F1 = 1
#   F2 = 1
#   F3 = 2
#   F4 = 3
#   F5 = 5
#   F6 = 8
#   F7 = 13
#   F8 = 21
#   F9 = 34
#   F10 = 55
#   F11 = 89
#   F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Answer: 4782
# ---------------------------------------------------------------------------

import time

# Records the start time of the screipt
start = time.time()

# Variable declaration 
a = 1 
b = 2 
fib = 1 
term = 3

while True:

    # Calculates the next number in the sequence
    fib = a + b
    
    # Prepares variables for the next loop iteration
    a = b
    b = fib
    term = term + 1
    
    # Converts current # to a strring so the len() function can be used on it 
    s = str(fib)
    
    # Checks length of current number, exiting if it is 1000 digits long 
    if len(s) == 1000:
        print('This is our number', term)
        
        # Records script end time, then calculates running time
        end = time.time()
        time_taken = end - start

        # Outputs script run time
        print()
        print('=================================')
        print('Script completed in {0:.2f} seconds.'.format(time_taken))
        exit() 
