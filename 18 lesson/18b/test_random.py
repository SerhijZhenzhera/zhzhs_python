'''
Task 2
The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
'''

import sys
from random import randint

if __name__ == "__main__":
    print(randint(1, 10))
    print(sys.path)


'''
---output---1---
7
['c:\\Users\\Regina\\Desktop\\3-8\\18b', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\python35.zip', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\DLLs', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\lib', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32', 'C:\\Users\\Regina\\AppData\\Roaming\\Python\\Python35\\site-packages', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages']
---output---2---
['1', '1']
['c:\\Users\\Regina\\Desktop\\3-8\\18b', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\python35.zip', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\DLLs', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\lib', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32', 'C:\\Users\\Regina\\AppData\\Roaming\\Python\\Python35\\site-packages', 'C:\\Users\\Regina\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages']
'''
