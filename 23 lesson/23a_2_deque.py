'''
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack

Дважды связанный список, в отличие от List
Операции .append() и .pop() осуществляются с постоянным времнем, зато поиск по индексу медленнее, чем у простого списка

List вообще не следует использовать в многопоточной среде
У Deque обе операции .append() и .pop() являются атомарными, то есть они не будут прерваны другим потоком. Однако в этом классе есть и другие методы,
которые специально не предназначены для атомарной работы и не являются поточно-ориентированными
'''

from collections import deque


def character_reverse(char):
    stack_1 = deque()
    for ch in char:
        stack_1.append(ch)
    print(stack_1)
    while True:
        try:
            print(stack_1.pop())
            print(stack_1)
        except IndexError:
            print('Stack is already empty...')
            return


if __name__ == '__main__':
    character_reverse('Violeta')
