'''
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack
'''


def character_reverse(char):
    stack_1 = []
    reverse_lit = ''
    for ch in char:
        stack_1.append(ch)
    print(stack_1)
    stack_2 = stack_1.copy()
    stack_3 = stack_1.copy()
    while True:
        try:
            print(stack_2.pop())
            print(stack_2)
        except IndexError:
            print('Stack is already empty...')
            break
    while True:
        try:
            reverse_lit += stack_3.pop()
            print(reverse_lit)
            print(stack_3)
        except IndexError:
            print('Stack is already empty...')
            return


if __name__ == '__main__':
    character_reverse('Violeta')
