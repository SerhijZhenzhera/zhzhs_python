'''
Task 3
Returns  a * n
'''

def mult(a, n):
    if n == 1:
        return a
    if n == 0:
        return 0
    if n < 0:
        return 'ValueError: This function works only with postive integers'
    return a + mult(a, n-1)


if __name__ == '__main__':

    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
    assert mult(2, -4) == 'ValueError: This function works only with postive integers'
