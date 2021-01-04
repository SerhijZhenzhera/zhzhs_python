'''
Task 3. A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
'''


def input_data():
    while True:
        operator = input('Choose the operator (+, -, *): ')
        if operator in ['+', '-', '*']:
            start_list = [operator]
            break
        else:
            print('Wrong operator!')
    while True:
        first_number = input('Choose first number: ')
        if first_number[1:].isdigit() and first_number[:1] == '-' or first_number.isdigit():
            start_list.append(int(first_number))
            break
        else:
            print('Only numbers, please')
    while True:
        arg = input(
            'Choose another numbers by turn ("s" to complete): ').lower()
        if arg == 's':
            break
        elif arg[1:].isdigit() and arg[:1] == '-' or arg.isdigit():
            start_list.append(int(arg))
        else:
            print('Only numbers, please')
        start_tuple = tuple(start_list)
    return start_tuple


def make_operation(operator, first_number, *args):
    for arg in args:
        if operator == '+':
            first_number += arg
        elif operator == '-':
            first_number -= arg
        else:
            first_number *= arg
    print('Final result:', first_number)


start_tuple = input_data()
make_operation(*start_tuple)

'''
---input and output---
Choose the operator (+, -, *): j
Wrong operator!
Choose the operator (+, -, *): *
Choose first number: j
Only numbers, please
Choose first number: -1
Choose another numbers by turn ("s" to complete): 2
Choose another numbers by turn ("s" to complete): j
Only numbers, please
Choose another numbers by turn ("s" to complete): -3
Choose another numbers by turn ("s" to complete): 4
Choose another numbers by turn ("s" to complete): s
Final result: 24
'''
