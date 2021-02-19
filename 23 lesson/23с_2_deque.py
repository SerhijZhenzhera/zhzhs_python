'''
Task 3
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message

Extended:
32-34
z = Deque()
'''


class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def get_from_stack(self, e):
        get_index = self._items.index(e)
        return self._items.pop(get_index)

    def size(self):
        return len(self._items)

    def __repr__(self):
        return '<Deque> : ' + str(self._items)

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # d = Deque()
    z = Deque()

    z.add_front('1')
    z.add_front(1)
    z.add_front('#')
    z.add_front('sproba')
    print(z.size())
    print(z)
    print(z.get_from_stack('#'))
    print(z)

    '''
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
    print(d)
    '''
