'''
Задание 2. Математическая задача
- на базе Test 4 (урок 4)
- со случайным выбором простого математического действия без float
- с циклом из 5 повторов
'''

import random
i = 1
while i <= 5:
    a = random.randint(1, 35)
    b = random.randint(1, 35)
    add = a + b
    mult = a * b
    if a >= b:
        sub = a - b
    else:
        sub = b - a
    start = [add, sub, mult]
    r = random.choice(start)
    if r == add:
        print('Сколько будет:', a, '+', b, '?')
    elif r == sub and a >= b:
        print('Сколько будет:', a, '-', b, '?')
    elif r == sub and b > a:
        print('Сколько будет:', b, '-', a, '?')
    else:
        print('Сколько будет:', a, '*', b, '?')
    test = input()
    if test == 'Святослав':
        break
    elif test == 'Violeta':
        continue
    else:
        pass
    if test.isnumeric():
        test_int = int(test)
        if test_int == r:
            print('Правильно, это', r)
            i += 1
            continue
        else:
            print('Не верно, должно быть', r)
            i = 1
            continue
    else:
        print('Вводите только цифры, пожалуйста!')
        i = 1
        continue
print('Отлично! 5 правильных ответов подряд!')
