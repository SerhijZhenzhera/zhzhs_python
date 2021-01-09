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
        r = None
        for num in numbers:
            if not type(num) == int:
                r = 'stop'
                print('Operate only with numbers!')
            else:
                if operator == '+':
                    first_number += num
                elif operator == '-':
                    first_number -= num
                else:
                    first_number *= num
    if not r == 'stop':
        print('Final result:', first_number)


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
    numbers = input(
        'Choose another numbers by turn ("s" to complete): ').lower()
    if numbers == 's':
        break
    elif numbers[1:].isdigit() and numbers[:1] == '-' or numbers.isdigit():
        start_list.append(int(numbers))
    else:
        print('Only numbers, please')


print(start_list)  # test
make_operation(*start_list)  # it works with list and tuple the same way
# [https://devpractice.ru/python-lesson-8-tuple/]
start_tuple = tuple(start_list)  # if you need a tuple
print(start_tuple)  # test

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
['*', -1, 2, -3, 4]
Final result: 24
('*', -1, 2, -3, 4)
'''
