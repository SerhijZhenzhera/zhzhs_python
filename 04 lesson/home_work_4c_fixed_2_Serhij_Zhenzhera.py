'''
Task 3. Words combination. Create a program that reads an input string
and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’,
so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
'''

import random
test = input('Введите любое слово: ')
list_result = []
i = 1
if len(test) > 4:
    while i < 6:
        test_start = list(test)
        random.shuffle(test_start)
        test_result = ''.join(test_start)
        if not test_result in list_result:
            list_result.append(test_result)
            i += 1
        else:
            continue
    print(list_result)

else:
    print('Слишком короткое!')
