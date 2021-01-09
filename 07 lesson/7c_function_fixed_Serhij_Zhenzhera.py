'''
Task 3. A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
'''


def make_operation(operator, first_number, *numbers):
    if not operator in ['+', '-', '*']:
        print('Wrong operator!')
        return
    elif not type(first_number) == int:
        print('Operate only with numbers!')
        return
    else:
        r = True
        for num in numbers:
            if not type(num) == int:
                r = False
                print('Operate only with numbers!')
            else:
                if operator == '+':
                    first_number += num
                elif operator == '-':
                    first_number -= num
                else:
                    first_number *= num
    if r == True:
        print('Final result:', first_number)


make_operation('*', -1, -2, 3, 4)
make_operation('k', -1, -2, 3, 4)
make_operation('*', 'k', -2, 3, 4)
make_operation('*', -1, 'k', 3, 4)
make_operation('*', -1, -2, 'k', 4)
make_operation('*', -1, -2, 3, 'k')

'''
---output---
Final result: 24
Wrong operator!
Operate only with numbers!
Operate only with numbers!
Operate only with numbers!
Operate only with numbers!
'''
