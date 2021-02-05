'''
Task 1. File Context Manager class
Create your own class, which can behave like a built-in function `open`. Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method, which has to cover all the requirements to context managers mentioned here:
https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager 
https://docs.python.org/3.7/reference/compound_stmts.html#with
'''


class Open:
    counter = 0

    @classmethod
    def num_of_usage(cls):
        return cls.counter

    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
        except:
            FileNotFoundError
            print('Wrong address!')

    def __enter__(self):
        Open.counter += 1
        try:
            return self.file_obj
        except:
            AttributeError

    def __exit__(self, type, value, traceback):
        try:
            self.file_obj.close()
            print('Was opened', self.counter, 'times')
        except:
            AttributeError
            print('Exception has been handled...')
            return True  # иначе test = opened_file.read() AttributeError: 'NoneType' object has no attribute 'read'


if __name__ == "__main__":

    with Open('demo.txt', 'r') as opened_file:
        test = opened_file.read()
        print(test)

    with Open('demo1.txt', 'r') as opened_file:
        test = opened_file.read()
        print(test)

'''
---output---
Regina
Was opened 1 times
Wrong address!
Exception has been handled...
'''
