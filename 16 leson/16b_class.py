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
        else:
            result = self.start
            self.start += self.step
        # print(result) # можно увидеть, что результаты генерируются до 10 15 20 25 --> OK
        return result

# специальный вывод экземпляра на печать не нужен - он создаётся только для и до решения задачи поиска

if __name__ == "__main__":

    if 25 in InRange(10, 100, 5):
        print('OK')
    
    print(*InRange(10, 100, 5))

    b = InRange
    print(*b(1, 12))
    print(*b(1, 12, 3))
    print(*b(1, '5'))
    

'''
---output---
OK
10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
1 2 3 4 5 6 7 8 9 10 11 12
1 4 7 10
Use only numbers!
Traceback (most recent call last):
  File "r:\Beetroot\Python\16\16b_check_Serhij_Zhenzhera.py", line 41, in <module>
    print(*b(1, '5'))
  File "r:\Beetroot\Python\16\16b_check_Serhij_Zhenzhera.py", line 16, in __init__
    raise TypeError
TypeError
'''
