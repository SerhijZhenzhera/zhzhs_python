'''
Task 5
Sum of digits
'''

def sum_of_digits(digit_string):
    if len(digit_string) == 0:
        return 0
    try:
        return int(digit_string[len(digit_string)-1]) + sum_of_digits(digit_string[:len(digit_string)-1])
    except:
        ValueError
        return 'ValueError("input string must be digit string")'


if __name__ == '__main__':

    assert sum_of_digits('26') == 8
    assert sum_of_digits('test') == 'ValueError("input string must be digit string")'
    assert sum_of_digits('12345') == 15
