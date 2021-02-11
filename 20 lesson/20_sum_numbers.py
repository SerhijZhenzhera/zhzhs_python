'''
In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters
Input: A string.
Output: An int. 
'''

# comment syntax (Python 3.5 and earlier)


def sum_numbers(text: str) -> 'sum of numbers in ints, but not numbers in words':
    words = text.split()  # str -> list
    result = 0  # int
    for word in words:
        try:  # int inside word
            result += int(word)
        except:  # str inside word
            ValueError
    return result  # sum of numbers in ints


print(sum_numbers.__annotations__)


if __name__ == '__main__':

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0

'''
---output---
{'text': <class 'str'>, 'return': 'sum of numbers in ints, but not numbers in words'}
'''


# from typing import List, Optional (Python 3.9+)

def sum_numbers(text: str) -> Optional[int]:
    words: List[str] = text.split()
    result: Optional[int] = 0
    for word in words:
        try:
            result: += int(word)
        except:  # str inside word
            ValueError
    return result: int


# install mypy

def sum_numbers(text):
    words = text.split()
    result = 0
    for word in words:
        result += int(word)  # TypeError: can only add int (not "str") to int
    return result
