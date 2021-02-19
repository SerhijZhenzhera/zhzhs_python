'''
Task 3
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message

Extended:
26-28
z = Stack()
'''


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def get_from_stack(self, e):
        get_index = self._items.index(e)
        return self._items.pop(get_index)

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack> ->  "
        for ind, item in enumerate(reversed(self._items), 1):
            representation += (str(ind) + ':' + str(item) + '  ')
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # s = Stack()
    z = Stack()

    z.push('1')
    z.push(1)
    z.push('#')
    z.push('sproba')
    print(z.size())
    print(z)
    print(z.get_from_stack('#'))
    print(z)

    '''
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)
    print(s.pop())
    print(s)
    '''
