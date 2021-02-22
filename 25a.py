def binary_search(obj: list, item: int, j=1):
    obj = sorted(obj)
    if len(obj) == 0 and j % 10 != 1:
        return str(item) + ' was not found (by ' + str(j) + ' steps)'
    if len(obj) == 0 and j % 10 == 1:
        return str(item) + ' was not found (by ' + str(j) + ' step)'
    mid = len(obj)//2  # можно обойтись без этой переменной obj[:len(obj)//2]
    guess = obj[mid]
    if guess == item:
        return 'It took ' + str(j) + ' steps to find: ' + str(item)
    if guess > item:
        obj = obj[:mid]
        return binary_search(obj, item, j+1)
    if guess < item:
        obj = obj[mid+1:]
        return binary_search(obj, item, j+1)


if __name__ == '__main__':

    print(binary_search([1, 3, 5, 7, 9], 3))
    print(binary_search([1, 3, 5, 7, 9], -10))
    print(binary_search([7, 5, 1, 3, 2], 6))
    print(binary_search([7, 5, 1, 3, 2], 7))
    print(binary_search([7, 5, 1, 3, 2], 9))
    print(binary_search([], 0))

    print(binary_search([10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130], 60))


'''
---output---
It took 2 steps to find: 3
-10 was not found (by 4 steps)
6 was not found (by 4 steps)
It took 2 steps to find: 7
9 was not found (by 3 steps)
0 was not found (by 1 step)
It took 4 steps to find: 60
'''
