'''
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack

В отличие от deque, LifoQueue разработан так, чтобы быть полностью поточно-ориентированным. Все его методы безопасны для использования в многопоточной среде.
Он также добавляет дополнительные тайм-ауты для своих операций, которые часто могут быть обязательной функцией в многопоточных программах.
Однако такая полная безопасность потоков обходится дорого. Чтобы достичь этой безопасности, LifoQueue должен выполнять немного больше работы над каждой операцией,
а это значит, что это займет немного больше времени. Зачастую это небольшое замедление не влияет на общую скорость вашей программы,
но если вы измерите свою производительность и обнаружите, что ваши операции со стеком являются узким местом, тогда стоит осторожно перейти на deque

'''

from queue import LifoQueue


def character_reverse(char):
    stack_1 = LifoQueue()
    for ch in char:
        stack_1.put(ch)
    print(stack_1)  # распечатка объекта, а не содержимого
    while True:
        try:
            print(stack_1.get())
        except IndexError:
            print('Stack is already empty...')
            return


if __name__ == '__main__':
    character_reverse('Violeta')
