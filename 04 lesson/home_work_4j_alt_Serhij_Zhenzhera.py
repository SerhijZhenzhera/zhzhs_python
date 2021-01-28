'''
Задание 6. Для вводимых пользователем чисел отбираем минимальное и максимальное
'''

i = 1
min_user_num, max_user_num = None, None
while True:
    test = input('Введите число: ')
    if test[1:].isdigit() and test[:1] == '-' or test.isdigit():
        r = int(test)
        min_user_num = r if not min_user_num or min_user_num > r else min_user_num
        max_user_num = r if not max_user_num or max_user_num < r else max_user_num
        i += 1
        print('На данный момент максимум: ', max_user_num, ', минимум: ', min_user_num, ', раундов: ' , i-1, sep='')
    else:
        print('Вводите только цифры, пожалуйста!')
