'''
Task 3. Using python as a calculator. Make a program with 2 numbers saved in separate variables a and b,
then print the result for each of the following: 
    Addition
    Subtraction
    Division
    Multiplication
    Exponent (Power)
    Modulus
    Floor division
'''

a = 33
b = -7
print('Addition =', a + b)
print('Subtraction =', a - b)
print('Division =', a / b, 'or', end=' ')
print(format(a / b, '.3f'))
print('Multiplication =', a * b)
print('Exponent (Power) =', a ** b, 'or', end=' ')
print(format(a ** b, '.1f'))
print('Modulus :', abs(a), 'and', abs(b))
print('Floor division =', a // b)
