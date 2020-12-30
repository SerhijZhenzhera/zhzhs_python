'''
Task 3. A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
'''

while True:
    operator = input('Choose the operator (+, -, *): ')
    if operator in ['+', '-', '*']:
        break
    else:
        print('Wrong operator!')
result = None
while True:
    numbers = input('Choose numbers by turn ("r" to complete): ').lower()
    if numbers == 'r':
        if result == None:
            print("You have chosed nothing")
        else:
            print('You result is:', result)
            break
    elif numbers[1:].isdigit() and numbers[:1] == '-' or numbers.isdigit():
        numbers = int(numbers)
        if result == None:
            result = numbers
        else:
            if operator == '+':
                result += numbers
            elif operator == '-':
                result -= numbers
            else:
                result *= numbers
    else:
        print('Only numbers, please')
