'''
Task 2. Input data: ... Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.. 
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

fruits_names = list(stock.keys())
fruits_prices = list(stock.values())
money_names = list(prices.keys())
money_prices = list(prices.values())
total_price = 0
for i in range(len(stock)):
    ii = money_names.index(fruits_names[i]) # если последовательность элементов перепутали
    general_price = fruits_prices[i] * money_prices[ii]
    if general_price > 0:
        print(fruits_names[i], '=',general_price)
        total_price += general_price
    else:
        print('we have any', fruits_names[i], 'presently!')
print('the total price of stock =', total_price)

'''
---output---
banana = 24
we have any apple presently!
orange = 48.0
pear = 45
the total price of stock = 117.0
'''
