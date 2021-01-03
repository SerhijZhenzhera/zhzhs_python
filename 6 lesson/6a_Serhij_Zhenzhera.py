'''
Task 1. Make a program that has some sentence (a string) on input
and returns a dict containing all unique words as keys and the number of occurrences as values. 
'''

string_test = input('Введите какую-нибудь фразу: ').lower()
for i in range(len(string_test)):
    if string_test[i:i+1].isalpha() != True and string_test[i:i+1] != ' ':
        string_test = string_test[:i] + string_test[i+1:]
list_test = string_test.split()

from collections import Counter
dict_test = Counter(list_test)
print(dict_test)
dict_result = dict(dict_test)
print(dict_result)

'''
---input--- To be or not to be, that is a question
---output---
Counter({'to': 2, 'be': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'a': 1, 'question': 1})
{'to': 2, 'be': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'a': 1, 'question': 1}
'''
