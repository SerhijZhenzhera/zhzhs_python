'''
Task 3. List comprehension exercise. Use a list comprehension to make a list containing tuples (i, j)
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
'''

result = [(i, i*i) for i in range(10)]
print(result)

'''
---output---
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
'''
