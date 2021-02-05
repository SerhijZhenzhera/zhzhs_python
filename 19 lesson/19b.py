'''
Task 2. Writing tests for context manager
Take your implementation of the context manager class from Task 1 and write tests for it.
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you have errors in the runtime context suite.
'''

import unittest
from context_manager import Open


class OpenTestCase(unittest.TestCase):

    def test_file_existance(self):
        op_1 = Open('demo1.txt', 'r')
        op_2 = Open('demo.txt', 'r')
        with op_1, op_2 as opened_file:
            test = opened_file.read()
        self.assertTrue(Open, True)

    def test_counter(self):
        op_1 = Open('demo1.txt', 'r')
        op_2 = Open('demo.txt', 'r')
        with op_1 as opened_file:
            test = opened_file.read()
        with op_2 as opened_file:
            test = opened_file.read()
        with Open('demo.txt', 'r') as opened_file:
            test = opened_file.read()
            print(test)
        self.assertEqual(Open.counter, 3)


if __name__ == "__main__":

    unittest.main()


'''
---output---
Wrong address!
Exception has been handled...
Was opend 2 times
Regina
Was opend 3 times
.Wrong address!
Was opend 5 times
Exception has been handled...
.
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
'''
