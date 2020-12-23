'''
Задание 6. Для вводимых пользователем чисел отбираем минимальное и максимальное
'''

i = 1
while True:
    test = input('Введите число: ')
    if test[1:].isdigit() and test[:1] == '-' or test.isdigit():
        r = int(test)
        j = r if i == 1 else j
        k = r if i == 1 else k
        j = r if r > j else j
        k = r if r < k else k
        i += 1
        print('На данный момент максимум: ', j, ', минимум: ', k, ', раундов: ' , i-1, sep='')
    else:
        print('Вводите только цифры, пожалуйста!')
