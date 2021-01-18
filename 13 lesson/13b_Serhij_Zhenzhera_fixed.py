'''
Task 2. Write a Python program to access a function inside a function
(Tips: use function, which returns another function)   
'''

def f_1(a):
    return a

def f_2(b):
    def f_3(a):
        return(a)
    return b


if __name__ == "__main__":
    result = f_2(f_1)
    print(result(7))



'''
---output---
7
'''
