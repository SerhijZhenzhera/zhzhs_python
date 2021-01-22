'''
Task 1. Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
'''

from functools import wraps

def dec(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func)
        for arg in args:
            print(arg)
        for kwarg, value in kwargs.items():
            print(f'{kwarg}: {value}')    
        return func(*args, **kwargs)
    return wrapper


@dec
def do_nothing(*args, **kwargs):
    pass


if __name__ == "__main__":
    do_nothing(1, 'one', [1, 2, 3, 4, 5], a=1, b=2)


'''
---output---
<function do_nothing at 0x0000021BA21CCB80>
1
one
[1, 2, 3, 4, 5]
a: 1
b: 2
'''
