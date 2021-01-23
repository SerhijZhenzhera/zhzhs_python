'''
Task 3. Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):
methods:
    to_int
    to_str
    to_bool
    to_float
Don't forget to use @wraps
'''

from functools import wraps


class TypeDecorators:

    def __init__(self, function):
        self.function = function

    @staticmethod
    def to_int(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            info = function(*args, **kwargs)
            result = 'ooops!'
            try:
                result = int(info)
            except:
                TypeError
            return result
        return wrapper

    @staticmethod
    def to_str(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper

    @staticmethod
    def to_float(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            info = function(*args, **kwargs)
            result = 'ooops!'
            try:
                result = float(info)
            except:
                TypeError
            return result
        return wrapper

    @staticmethod
    def to_bool(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = bool(function(*args, **kwargs))
            return result
        return wrapper


@TypeDecorators.to_int
def do_something(string: str):
    return string


@TypeDecorators.to_str
def do_anything(string: str):
    return string


@TypeDecorators.to_float
def do_strange(string: str):
    return string


@TypeDecorators.to_bool
def do_nothing(string: str):
    return string


if __name__ == "__main__":
    print(do_something('25'))
    print(do_anything('True'))
    print(do_strange('0'))
    print(do_nothing(None))

'''
---output---
25
True
0.0
False
'''
