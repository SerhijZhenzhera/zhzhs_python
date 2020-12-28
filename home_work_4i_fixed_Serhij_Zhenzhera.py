'''
Задание 5. Пишем в цикле решение уравнения аx**2+bx+c=0 рассчитываем ответ
'''
from math import sqrt
i = 0
while True:
    z = input('Хотите решить уравнение? Y/N ').lower()
    if z == 'y':
        pass
    elif z == 'n':
        break
    else:
        continue
    a = input('Введите коэффициент a: ')
    try:
        a = float(a)
    except ValueError:
        print('Вводите только числа, пожалуйста')
        continue
    b = input('Введите коэффициент b: ')
    try:
        b = float(b)
    except ValueError:
        print('Вводите только числа, пожалуйста')
        continue
    c = input('Введите коэффициент c: ')
    try:
        c = float(c)
    except ValueError:
        print('Вводите только числа, пожалуйста')
        continue
    d = b**2 - 4*a*c
    i += 1
    print('Ршешение №', i) # тест
    if d > 0:
        print('x_1=', (-b + sqrt(d)) / (2*a), ', x_2=', (-b - sqrt(d)) / (2*a))
    elif d == 0:
        print('x= ', -b / (2*a))
    else:
        print('Извините, но вещественных корней у такого уравнения не будет. Задействуйте комплексные числа')
print('Спасибо!')

'''
Извлечение квадратного корня [https://all-python.ru/osnovy/korni.html]
---1---
from math import sqrt
x = sqrt(4)
print(x)
2.0
---2---
n = 2
x = 4**(1./n)
print(x)
2.0
---3---
x = pow(4, 0.5)
print(x)
2.0
'''
