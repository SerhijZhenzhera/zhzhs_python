'''
Task 2. Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b,
construct a try-except block which raises an exception if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).    
'''


def divider(a, b):
    try:
        d = int(a)**2 / int(b)
        # return d
        print('%.2f' % d)
    except ValueError:
        print('Use only numbers, please!')
        raise
    except ZeroDivisionError:
        print('Cannot be divided by zero!')
        raise


a = input('Enter dividend to square: ')
b = input('Enter divider: ')
divider(a, b)
