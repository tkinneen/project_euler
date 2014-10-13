#!/usr/bin/python
# Project Euler - Problem 16
# Author: Timothy Kinneen
# Version 1.0.1 
# ------------------------------------------------------------------
# Description:
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# Answer: 1366
# ------------------------------------------------------------------

import time

# Records the time the script is started
start = time.time()

sum = 0
result = 1

# Loops until 2 is raised to the thousandth power
for x in range(1, 1001):
    result = result * 2

# The result is converted to a string so we can manipulate individual digits
result = str(result)

# We loop through the individual digits in the result, convert each one
# back to an integer, then add it to the sum total
for x in result:
    x = int(x)
    sum = sum + x

print('Answer: ', sum)
   
# Records script end time, then calculates running time
end = time.time()
time_taken = end - start

# Outputs script run time
print()
print('=================================')
print('Script completed in {0:.2f} seconds.'.format(time_taken))
