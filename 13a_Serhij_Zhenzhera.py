'''
Task 1. Write a Python program to detect the number of local variables declared in a function   
'''

e = 5
def secret(a, d):
    a = 7
    b = '7'
    c = 'seven'
    f = a + e


if __name__ == "__main__":
    print(secret.__code__.co_nlocals) # число локальных переменных, используемых функцией (включая аргументы)
    print(secret.__code__.co_names) # кортеж нелокальных имен, на которые есть ссылки в теле функции
    print(secret.__code__.co_varnames) # кортеж имён переменных (от аргументов до локальных)
    print(secret.__code__.co_consts) # кортеж литералов, встречающихся в теле функции


'''
---output---
5
('e',)
('a', 'd', 'b', 'c', 'f')
(None, 7, '7', 'seven')
'''
