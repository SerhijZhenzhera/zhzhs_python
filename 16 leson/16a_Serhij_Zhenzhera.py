'''
Task 1. Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
'''

import random

def with_index(iterable, start=0, bonus=(1, 100)):
    try:
        for iter in iterable:
            personal_bonus = random.randint(*bonus)
            # print(start+1, iter)
            yield(start, iter, personal_bonus)
            start += 1
    except:
        TypeError
        print('Is not iterable!')



if __name__ == "__main__":
    print(*with_index(['a', 'b', 'c', 'd', 'e']))
    print(*with_index(['a', 'b', 'c', 'd', 'e'], 3))
    print(*with_index(12345))


'''
---output---
(1, 'a', 65) (2, 'b', 21) (3, 'c', 78) (4, 'd', 6) (5, 'e', 5)
(3, 'a', 30) (4, 'b', 12) (5, 'c', 2) (6, 'd', 55) (7, 'e', 9)
Is not iterable!
'''
