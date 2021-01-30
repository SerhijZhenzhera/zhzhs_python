'''
Task 3. Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
'''

class IterForIn:

    def __init__(self, *iterable):
        self.iterable = list(iterable)

    def __iter__(self): 
        try:
            i = 0
            while True:
                yield(self.iterable[i])
                i += 1
        except:
            StopIteration

    def __getitem__(self, key):
        try:
            return self.iterable[key]
        except:
            IndexError
            print('Out or range! Index should be < len of object')        
    
    def __str__(self):
        return '{self}'.format(self=self.iterable)


if __name__ == "__main__":
    b = IterForIn(1,2,3,"432", 433, {1,2,3})
    for i in b:
        print(i)

    print(b)
    print(b[2])
    print(b[5])
    print(b[7])



'''
---output---
1
2
3
432
433
{1, 2, 3}
[1, 2, 3, '432', 433, {1, 2, 3}]
3
{1, 2, 3}
Out or range! Index should be < len of object
None
'''
