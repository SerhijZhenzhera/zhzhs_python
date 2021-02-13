'''
Смоделировать на списке прибавление единички к числу
'''

def add_one(my_list):
    num_str = ''
    for ml in my_list:
        num_str += str(ml)
    num_digit = int(num_str)
    result_digit = num_digit + 1
    result_str = str(result_digit)
    return list(result_str)


print(add_one([9, 9, 9]))
