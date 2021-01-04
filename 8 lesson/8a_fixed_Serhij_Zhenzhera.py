'''
Task 1. Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
'''

'''
В функции inside_try исключение перехватывается с помощью pass, print, другой произвольной функции...
Но функция oops, вызывая своё исключение, видимо требует упонимания ещё и того исключения, которое перехватила - 
в результате она всё равно сообщает о перехвате исключения, выводя сразу два
'''


def oops(some_err):
    if some_err == IndexError:
        raise some_err


def inside_try():
    string_try = input('Enter something: ')
    try:
        for i in range(len(string_try) + 1):
            print(string_try[i])  # test
    except IndexError:
        oops(IndexError)
    finally:
        print('Tested!')


inside_try()


'''
---output for IndexError in oops()---
Enter something: abc
a
b
c
Tested!
Traceback (most recent call last):
  File "c:/Serhij/Beetroot/Python/8/8a_1_Serhij_Zhenzhera.py", line 23, in inside_try
    print(string_try[i])  # test
IndexError: string index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:/Serhij/Beetroot/Python/8/8a_1_Serhij_Zhenzhera.py", line 34, in <module>
    inside_try()
  File "c:/Serhij/Beetroot/Python/8/8a_1_Serhij_Zhenzhera.py", line 27, in inside_try
    oops(err)
  File "c:/Serhij/Beetroot/Python/8/8a_1_Serhij_Zhenzhera.py", line 16, in oops
    raise some_err
IndexError
----------------------------------------------------------------------------------
---output for KeyError in oops()---
Enter something: abc
a
b
c
Tested!
'''
