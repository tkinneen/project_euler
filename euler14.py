#!/usr/bin/python
# Project Euler - Problem 14
# Author: Timothy Kinneen
# Version: 1.0.1
# ------------------------------------------------------------------
# Description:
#
# The following iterative sequence is defined for the set of positive integers:
#
#     n → n/2 (n is even)
#     n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Answer: 
# ------------------------------------------------------------------

import time

start = time.time()

starting_num = []
biggest = 1
chain = 0

# Loop through each number between 2 and one million
for x in range(2, 1000001):
    
    # If a chain breaks the current record, this variable will tell us
    # what number the chain started on 
    origin = x 
    
    # Collatz sequence will loop until we reach 1 
    while x != 1:
        
        # Different actions are performed if the current # is even or odd
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        
        # Each loop adds to the chain by 1
        chain = chain + 1
    
    # If this is the largest chain yet, 'biggest' variable is updated 
    if chain > biggest:
        biggest = chain
        
        # The number started on is recorded when a record is broken
        starting_num.insert(0, origin) 
    chain = 0

print(biggest)
print('Starting number of the largest Collatz chain under 1,000,000: ', starting_num[0])

# Records and outputs the script's starting time
end = time.time()
final = end - start
print()
print('----------------------------------------')
print("Script took {0:.2f} seconds".format(final))
 
