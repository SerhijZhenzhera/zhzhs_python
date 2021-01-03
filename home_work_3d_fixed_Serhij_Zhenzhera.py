'''
Задание 1. Получить от пользователя его номер телефона, проверить подходит ли номер под форматы
+380_________ (прочерки - любая цифра)
0_________ (например 0931233232)
0__ ___ __ __ (пробелы именно пробелы и телефон например 095 321 12 21)
Если номер введен верно - похвалите человека. Если нет - поругайте
'''

while True:
    number_tel = input('Введите номер телефона: ')
    number_tel = ''.join(number_tel.split())
    if number_tel[:1] != '0':
        print('Начните номер с нуля')
        continue
    elif len(number_tel) > 10:
        print('Номер должен состоять из 10 цифр')
        continue
    elif len(number_tel) < 10:
        print('Вы пропустили несколько цифр')
        continue
    else:
        number_tel = number_tel[1:10]
        if number_tel.isnumeric():
            print('Спасибо! Вы ввели номер: +380', number_tel[:2], number_tel[2:5], number_tel[5:7], number_tel[7:9])
        else:
            print('Вводите только цифры, пожалуйста')
  