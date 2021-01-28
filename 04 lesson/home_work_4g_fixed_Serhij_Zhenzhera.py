'''
Задание 3. Пока пользователь не введет Q - но не больше 5 раз - запрашиваем у пользователя число.
В конце принтуем максимальное введенное. Если введет не число, попытка ввода НЕ засчитывается. 
'''

i = 1
j = None
while i <= 5:
    maximum = input('Введите число (для выхода введите Q): ').upper()
    if maximum == 'Q':
        break
    elif maximum[1:].isdigit() and maximum[:1] == '-' or maximum.isdigit():
        mxm = int(maximum)
        j = mxm if not j or mxm > j else j
        i += 1
    else:
        print('Вводите только цифры, пожалуйста!')
print('Максимальное значение:', j)
