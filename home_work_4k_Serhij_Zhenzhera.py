'''
Задание 7. Камень-ножницы-бумага пока не надоест (Q). Загадываем и спрашиваем пользователя, что он загадал.
Плюсуем себе или ему победу - и так по кругу. Принтуем общий счет.
'''

import random
i = 1
j = 1
k = 1
while True:
    a = random.randint(1, 3)
    b_input = input('Камень, ножницы, бумага? (для выхода - Q): ' ).lower()
    if b_input == 'q':
        break        
    elif b_input == 'камень':
        if a == 1:
            print('Ничья')
            i += 1
        elif a == 2:
            print('Вы победили!')
            k += 1
        elif a == 3:
            print('Победа наша!')
            j += 1
    elif b_input == 'ножницы':
        if a == 2:
            print('Ничья')
            i += 1
        elif a == 3:
            print('Вы победили!')
            k += 1
        elif a == 1:    
            print('Победа наша!')
            j += 1    
    elif b_input == 'бумага':
        if a == 3:
            print('Ничья')
            i += 1
        elif a == 1:    
            print('Вы победили!')
            k += 1
        elif a == 2:
            print('Победа наша!')
            j +=1
    else:
        print('Выберите один из трёх вариантов, пожалуйста')     
print('Спасибо! ', 'Ваших побед: ', k-1, ', наших: ', j-1, ', ничьих: ', k-1, sep='')            
           