'''
Task 3. Extracting numbers. Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
Finally, print the list.
'''

list_a = []
list_b = []
i = 0
while i <= 99:
    i += 1
    a = i
    list_a.append(a)
    if i % 7 == 0 and i % 5 != 0:
        b = i
        list_b.append(b)
print('1-100 integers list:', list_a) # test
print('Task list:', list_b)
           