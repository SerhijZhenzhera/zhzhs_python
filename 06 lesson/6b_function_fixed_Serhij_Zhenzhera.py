'''
Task 2. Input data: ... Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock..
-------
Дополнительное задание. Решить через dict.key, чтобы учесть полное отсутствие произвольного ключа в словаре 
'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def total_price(goods, money):
    sum_price = 0
    for key in goods:
        general_price = goods.get(key, 0) * money.get(key, 0)
        if general_price > 0:
            print(key, '=', general_price)
            sum_price += general_price
        else:
            print('we have any', key, 'presently...')
    print('The total price of stock =', sum_price)
   
total_price(stock, prices)  

'''
---output---
banana = 24
we have any apple presently...
orange = 48.0
pear = 45
The total price of stock = 117.0
'''
