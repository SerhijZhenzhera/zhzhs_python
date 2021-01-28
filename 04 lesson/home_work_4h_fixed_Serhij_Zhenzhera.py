'''
Задание 4. В цикле получаем число, потом действие, потом опять число и снова действие, пока не получим Q.
Действия "+" или "-".
Выполняем действие и выводим результат (если введет не число или не действие - игнорируем и перезапрашиваем снова)
'''

import random
i = 1
mistakes = 1
while True:
    num_random = random.randint(1, 100)
    b_input = input('Введите число (для выхода введите Q): ')
    if b_input == 'Q':
        break
    elif b_input[:1] == '-':
        print('Значения должны быть больше нуля')
        continue
    elif b_input.isnumeric():
        b_player = int(b_input)
    else:
        print('Вводите только цифры, пожалуйста!')
        continue 
    add = num_random + b_player
    if num_random >= b_player:
        sub = num_random - b_player
    else:
        sub = b_player - num_random
    start = [add, sub]
    random_task = random.choice(start)
    if random_task == sub and num_random >= b_player:
        print('Сколько будет:', num_random, '-', b_player, '?')
    elif random_task == sub and b_player > num_random:
        print('Сколько будет:', b_player, '-', num_random, '?')
    else:
        print('Сколько будет:', num_random, '+', b_player, '?')
    test = input()
    if test == 'Q':
        break
    if test.isnumeric():
        test_int = int(test)
        if test_int == random_task:
            print('Правильно, это', random_task)
            i += 1
            continue
        else:
            print('Не верно, должно быть', random_task)
            mistakes += 1
            continue
    else:
        print('Вводите только цифры, пожалуйста!')
        continue
print('Спасибо! ', 'Правильных ответов: ', i-1, '. Неверных ответов: ', mistakes-1, sep='')
