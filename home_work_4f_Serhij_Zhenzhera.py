'''
Задание 2. Спросить у пользователя, сколько попыток и до скольки максимум пробовать.
Сделать генерацию рендомного значения столько-то раз.
Каждое значение вывести и потом вывести итоговое максимально выпавшее число.
'''

quantity = input('Введите количество попыток: ')
maximum = input('Введите максимальное значение: ')
if quantity[:1] == '-' or maximum[:1] == '-':
    print('Значения должны быть больше нуля')
elif quantity.isdigit() and maximum.isdigit():
    import random
    qnt, mxm = int(quantity), int(maximum)
    i = 1
    j = 1
    while qnt >= i:
        result = random.randint(1, mxm)
        print(result)
        i += 1
        j = result if result > j else j
    print('Максимальное значение:', j)
else:
    print('Вводите только цифры, пожалуйста!')
