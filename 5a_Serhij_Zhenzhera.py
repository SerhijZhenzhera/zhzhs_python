'''
Task 1. The greatest number.
Write a Python program to get the largest number from a list of random numbers with the length of 10.
Constraints: use only while loop and random module to generate numbers.
'''

import random
list = []
i = 1
while i <= 10:
    a = random.random()
    list.append(a)
    i += 1
print(list)
print(max(list))
           