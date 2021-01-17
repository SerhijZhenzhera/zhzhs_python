'''
Task 2. Write a Python program to access a function inside a function
(Tips: use function, which returns another function)   
'''

# external access
def secret_1(a):
    b = 7
    c = a + b
    return c

def return_secret():
    return secret_1(6)


# access from the inside
def secret_2(a):
    b = 7
    c = 1
    def nested_secret():
        nonlocal c
        c += 2
        d = c*(a + b)
        return d
    return nested_secret()


if __name__ == "__main__":
    print(return_secret()) # for the external access
    print(secret_2(6)) # for access from the inside


'''
---output---
13
39
'''
