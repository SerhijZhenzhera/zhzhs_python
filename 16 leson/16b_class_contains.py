'''
Task 2. Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
'''


class InRange:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        if not type(start) == type(end) == type(step) == int:
            print('Use only numbers!')
            raise TypeError
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        result = self.start
        self.start += self.step
        return result

    def __contains__(self, num):
        if num in list(self):
            return f'OK {num} in range'
        else:
            return f'not {num} in range'
            

if __name__ == "__main__":
   
    b = InRange(10, 100, 5)
    print(b.__contains__(13))
    print(b.__contains__(25))
    print(13 in b)
    print(25 in b)
    

'''
---output---
not 13 in range
not 25 in range
True
True
'''
