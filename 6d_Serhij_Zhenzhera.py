'''
Задание 1. Сделайте словарь дней недели {1: "Monday", 2:... } в общем словарь.
И потом "переверните" чтоб было {"Monday": 1, ... 
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dict_days_numbers = {days[i]: i+1 for i in range(7)}
print(dict_days_numbers)

days_dict_numbers = dict(zip(dict_days_numbers.values(), dict_days_numbers.keys()))
print(days_dict_numbers)

'''
---output---
{'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
{1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
'''
