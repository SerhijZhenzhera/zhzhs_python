'''
Task 4. The math quiz program. Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong, and then responds with a message accordingly.
'''

import random
a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = a + b
print('Сколько будет:', a, '+', b, '?')
test = input()
if test.isnumeric():
    test_int = int(test)
    if test_int == c:
        print('Правильно, это', c)
    else:
        print('Не верно, должно быть', c)
else:
    print('Вводите только цифры, пожалуйста!')
