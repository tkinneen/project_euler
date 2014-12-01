#!/usr/bin/python
# Project Euler - Problem 3
# Author: Tim Kinneen 
# Version: 1.0.1
# -----------------------------------------------------------------
# Description:
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857 
# -----------------------------------------------------------------

import time

start = time.time()

num = 600851475143 
i = 2

# Loops until the square root of the target number is reached  
while i * i < num:
    # If the target number is evenly divisible by the current iterator, 
    # the target number can be reduced 
    while num % i == 0:
        num = num / i
    i = i + 1

# Outputs the answer
print("The answer is: ", num)  

# Calculates and outputs the script's running time
end = time.time()
final = end - start
print()
print('----------------------------------------')
print("Script took {0:.2f} seconds".format(final))
