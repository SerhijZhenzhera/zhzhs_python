'''
Task 3. Words combination. Create a program that reads an input string
and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’,
so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
'''

import random
test_1 = input('Введите любое слово: ')
if len(test_1) > 4:
    i = 1
    while(i < 6):
        test_2 = test_1[:5]
        test_3 = list(test_2)
        random.shuffle(test_3)
        test_4 = ''.join(test_3)
        print(test_4, end=' ')
        i = i + 1   
else:
    print('Слишком короткое!')
