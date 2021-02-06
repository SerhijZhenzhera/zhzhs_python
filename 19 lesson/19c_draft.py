'''
Task 3 (Optional)
Pytest fixtures with context manager
Create a simple function, which performs any logic of your choice with text data, which it obtains from a file object, passed to this function ( def test(file_obj) ).
Create a test case for this function using pytest library (https://docs.pytest.org/en/latest/contents.html).
Create pytest fixture, which uses your implementation of the context manager to return a file object, which could be used inside your function.
'''

import pytest
from context_manager import Open


def readdd(obj):
    file = open(obj, 'r')
    test = file.read()
    file.close()
    change = test.upper()
    print(change)


def test_reading():
    assert func('file_obj.txt') == 'REGINA'


if __name__ == "__main__":
    readdd('file_obj.txt')


'''
---output---

'''
