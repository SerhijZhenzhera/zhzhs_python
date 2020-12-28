'''
Task 1. String manipulation. Write a Python program to get a string made of the first 2 and the last 2 chars
from a given string. If the string length is less than 2, return instead of the empty string.
Tips:
    Use built-in function len() on an input string
    Use positive indexing to get the first characters of a string and negative indexing to get the last characters
'''

string_test = input('Введите что-нибудь не сильно короткое: ')
if len(string_test) >= 2:
    print('А вот во что из это получилось:', string_test[:2] + string_test[-2:])
else:
    print(' ')
