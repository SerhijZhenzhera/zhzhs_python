'''
Task 1
Returns  x ^ exp
'''

def to_power(x, exp):
    if exp == 1:
        return x
    if exp == 0 and x != 0:
        return 1
    if exp == 0 and x == 0:
        return 0
    if exp < 0:
        return 'ValueError: This function works only with exp > 0'
    return x * to_power(x, exp-1)


if __name__ == '__main__':

    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
    assert to_power(2, -1) == 'ValueError: This function works only with exp > 0'
    assert to_power(0, 3) == 0
    assert to_power(2, 0) == 1
