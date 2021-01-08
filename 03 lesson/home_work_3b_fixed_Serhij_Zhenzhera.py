'''
Task 2. The valid phone number program. Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
'''

number_tel = input('Введите номер телефона: ')
if number_tel.isnumeric():      
    if len(number_tel) < 10:
        print('Вы пропустили несколько цифр')
    elif len(number_tel) > 10:
        print('Номер должен состоять из 10 цифр')
    else:
        print('Спасибо! Вы ввели номер:', number_tel)
else:
    print('Вводите только цифры, пожалуйста')
   
