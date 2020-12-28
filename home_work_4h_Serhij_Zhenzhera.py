'''
Задание 4. В цикле получаем число, потом действие, потом опять число и снова действие, пока не получим Q.
Действия "+" или "-".
Выполняем действие и выводим результат (если введет не число или не действие - игнорируем и перезапрашиваем снова)
'''

import random
i = 1
j = 1
while True:
    a = random.randint(1, 100)
    b_input = input('Введите число (для выхода введите Q): ')
    if b_input == 'Q':
        break
    elif b_input[:1] == '-':
        print('Значения должны быть больше нуля')
        continue
    elif b_input.isnumeric():
        b = int(b_input)
    else:
        print('Вводите только цифры, пожалуйста!')
        continue 
    add = a + b
    if a >= b:
        sub = a - b
    else:
        sub = b - a
    start = [add, sub]
    r = random.choice(start)
    if r == sub and a >= b:
        print('Сколько будет:', a, '-', b, '?')
    elif r == sub and b > a:
        print('Сколько будет:', b, '-', a, '?')
    else:
        print('Сколько будет:', a, '+', b, '?')
    test = input()
    if test == 'Q':
        break
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
            j += 1
            continue
    else:
        print('Вводите только цифры, пожалуйста!')
        continue
print('Спасибо! ', 'Правильных ответов: ', i-1, '. Неверных ответов: ', j-1, sep='')
