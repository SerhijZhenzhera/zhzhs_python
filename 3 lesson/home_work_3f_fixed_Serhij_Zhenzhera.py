'''
Задание 3. Проверить что введенная строка является палиндромом
'''

string_test = input('Введите какую-нибудь фразу или слово: ').lower()
string_test_1 = ''.join(string_test.split()) # главную магию делает split, не вносящий в список пробелы
string_test_2 = string_test_1[::-1]
if string_test_2 == string_test_1: # if...== странновато: по-русски "если" уже содержит "ли", получается "если ... равно ли"
    print('Это палиндром!')
else:
    print('Это точно не палиндром...')

'''
Альтернативный вариант: (1) превратить сстроку в список .split(' '), (2) list.reverse(), (3) соединить в строку - join

https://python-scripts.com/reversed
    (1) text = 'TURBO'[::-1]
    (2) text = ''.join(reversed('TURBO'))
    (3) def reverse_string2(s):
            return "".join(reversed(s)) 
        data = reverse_string2('TURBO')
    (4) def reverse_string3(s):
            chars = list(s)
            for i in range(len(s) // 2):
                tmp = chars[i]
                chars[i] = chars[len(s) - i - 1]
                chars[len(s) - i - 1] = tmp
            return ''.join(chars)
        data = reverse_string3('TURBO')
'''
