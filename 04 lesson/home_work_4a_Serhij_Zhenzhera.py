'''
Task 1. The Guessing Game. Write a program that generates a random number between 1 and 10
and lets the user guess what number was generated. The result should be sent back to the user via a print statement.
'''

import random
number = random.randint(1, 10)
test = input('Загадайте число от 1 до 10: ')
if test.isnumeric():
    test_int = int(test)
    if number == test_int:
        print('Вы угадали! Это', test_int)
    else:
        print('Нет, это не', test_int, ', это' , number)
else:
    print('Вводите только цифры, пожалуйста!')        
