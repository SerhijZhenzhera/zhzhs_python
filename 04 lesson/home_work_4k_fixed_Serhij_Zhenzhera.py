'''
Задание 7. Камень-ножницы-бумага пока не надоест (Q). Загадываем и спрашиваем пользователя, что он загадал.
Плюсуем себе или ему победу - и так по кругу. Принтуем общий счет.
'''

import random
d = n = k = 1
game_result_1 = 'Победа наша!'
game_result_0 = 'Ничья'
game_result_2 = 'Вы победили!'
while True:
    a = random.randint(1, 3)
    b_input = input('Камень, ножницы, бумага? (для выхода - Q): ' ).lower()
    if b_input == 'q':
        break        
    elif b_input == 'камень':
        if a == 1:
            print(game_result_0)
            d += 1
        elif a == 2:
            print(game_result_2)
            k += 1
        elif a == 3:
            print(game_result_1)
            n += 1
    elif b_input == 'ножницы':
        if a == 2:
            print(game_result_0)
            d += 1
        elif a == 3:
            print(game_result_2)
            k += 1
        elif a == 1:    
            print(game_result_1)
            n += 1    
    elif b_input == 'бумага':
        if a == 3:
            print(game_result_0)
            d += 1
        elif a == 1:    
            print(game_result_2)
            k += 1
        elif a == 2:
            print(game_result_1)
            n +=1
    else:
        print('Выберите один из трёх вариантов, пожалуйста')     
print('Спасибо! ', 'Ваших побед: ', k-1, ', наших: ', n-1, ', ничьих: ', d-1, sep='')            
           