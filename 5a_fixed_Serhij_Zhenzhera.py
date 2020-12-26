'''
Task 1. The greatest number.
Write a Python program to get the largest number from a list of random numbers with the length of 10.
Constraints: use only while loop and random module to generate numbers.
'''

import random
list_r = []
i = 1
while i <= 10:
    a = random.random()
    list_r.append(a)
    i += 1
print(list_r)
print(max(list_r))
           