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

def total_price(offer, sales):
    goods_names = list(offer.keys())
    goods_prices = list(offer.values())
    money_names = list(sales.keys())
    money_prices = list(sales.values())
    total_price = 0
    for i in range(len(offer)):
        ii = money_names.index(goods_names[i]) # если последовательность элементов перепутали
        general_price = goods_prices[i] * money_prices[ii]
        if general_price > 0:
            print(goods_names[i], '=', general_price)
            total_price += general_price
        else:
            print('we have any', goods_names[i], 'presently...')
    print('The total price of stock =', total_price)
    return '(functions will be in the next lesson!)'
   
fruits = total_price(stock, prices)
print(fruits)    

'''
---output---
banana = 24
we have any apple presently...
orange = 48.0
pear = 45
The total price of stock = 117.0
(functions will be in the next lesson!)
'''
