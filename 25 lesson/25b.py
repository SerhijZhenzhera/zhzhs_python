# [https://medium.com/daily-python/implementing-fibonacci-search-algorithm-in-python-daily-python-27-4a6624366022]

def fib_search(arr, x):

    def fib_gen(n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            return fib_gen(n-1) + fib_gen(n-2)

    arr = sorted(arr)
    try:
        if x > arr[len(arr)-1]:
            return 'Search out of array!'
        if len(arr) == 1 and arr[0] == x:
            return str(x) + ' was found immediately!'
    except IndexError:
        return 'Array is empty...'
    m = 0
    j = 0
    k = 0
    offset = -1
    while fib_gen(m) < len(arr):
        m += 1
        j += 1
    while fib_gen(m) > 1:
        i = min(offset + fib_gen(m-2), len(arr)-1)
        # print('Current Element: ', arr[i])
        if x > arr[i]:
            k += 1
            m += 1
            offset = i
        elif x < arr[i]:
            k += 1
            m -= 2
        else:
            k += 1
            return str(x) + ' was found at index: ' + str(i) + ' by ' + str(j) + '_Fib_gen + ' + str(k) + '_Fib_search steps'
    # if fib_gen(m-1) and arr[offset+1] == x:
        # return offset + 1
    return str(x) + ' was not found by ' + str(j) + '_Fib_gen + ' + str(k) + '_Fib_search steps'


if __name__ == '__main__':

    print(fib_search([10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130], 60))

    print(fib_search([1, 3, 5, 7, 9], 3))
    print(fib_search([1, 3, 5, 7, 9], -10))
    print(fib_search([7, 5, 1, 3, 2], 6))
    print(fib_search([7, 5, 1, 3, 2], 7))
    print(fib_search([7, 5, 1, 3, 2], 9))
    print(fib_search([1, 2, 3], 1))
    print(fib_search([1, 3], 1))
    print(fib_search([2], 2))
    print(fib_search([2], 1))
    print(fib_search([], 0))


'''
---output---
60 was found at index: 6 by 7_Fib_gen + 6_Fib_search steps
3 was found at index: 1 by 5_Fib_gen + 1_Fib_search steps
-10 was not found by 5_Fib_gen + 2_Fib_search steps
6 was not found by 5_Fib_gen + 6_Fib_search steps
7 was found at index: 4 by 5_Fib_gen + 2_Fib_search steps
Search out of array!
1 was found at index: 0 by 4_Fib_gen + 1_Fib_search steps
1 was found at index: 0 by 3_Fib_gen + 1_Fib_search steps
2 was found immediately!
1 was not found by 1_Fib_gen + 0_Fib_search steps
Array is empty...
'''
