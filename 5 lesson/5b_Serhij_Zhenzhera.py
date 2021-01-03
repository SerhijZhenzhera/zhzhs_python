'''
Task 2. Exclusive common numbers. Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
'''

import random
list_1 = []
list_2 = []
i = 0
while i <= 19:
    i += 1
    if i <= 10:
        a = random.randint(1, 10)
        list_1.append(a)
    else:
        b = random.randint(1, 10)
        list_2.append(b)
list_3 = list(set(list_1 + list_2))
print(list_1) # test
print(list_2) # test
print(list_3)
           
