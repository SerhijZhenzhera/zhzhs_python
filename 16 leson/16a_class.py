'''
Task 1. Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
'''


class WithIndex:

    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        if not type(start) == int:
            print('Step only by numbers!')
            raise TypeError

    def __iter__(self):
        try:
            self.iterable[0]
        except:
            TypeError
            print('Is not iterable!') 
        try:
            i = 0
            while True:
                yield(self.start, self.iterable[i])
                self.start += 1
                i += 1
        except:
            StopIteration
        return self
    
    def __str__(self):
        return '{self}'.format(self=self.iterable)


if __name__ == "__main__":

    a = WithIndex
    print(a(['a', 'b', 'c', 'd', 'e']))
    print(a(['a', 'b', 'c', 'd', 'e'], 3))
    print(a(['a', 'b', 'c', 'd', 'e'], a))
    print(a(12345))


'''
---output---
(0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
(3, 'a') (4, 'b') (5, 'c') (6, 'd') (7, 'e')
Step only by numbers!
Traceback (most recent call last):
  File "r:\Beetroot\Python\16\16a_alt_Serhij_Zhenzhera.py", line 40, in <module>
    print(*a(['a', 'b', 'c', 'd', 'e'], a))
  File "r:\Beetroot\Python\16\16a_alt_Serhij_Zhenzhera.py", line 15, in __init__
    raise TypeError
TypeError
'''
