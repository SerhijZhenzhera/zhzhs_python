'''
Task 2
The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
'''


def randint(first, second):
    return list(str(first + second))


if __name__ == "__main__":
    print(randint(1, 10))


'''
---output---
['1', '1']
'''
