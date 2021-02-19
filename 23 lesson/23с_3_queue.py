'''
Task 3
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message

Extended:
26-28
z = Queue()
'''


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def get_from_stack(self, e):
        get_index = self._items.index(e)
        return self._items.pop(get_index)

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue> ->  "
        for ind, item in enumerate(reversed(self._items), 1):
            representation += (str(ind) + ':' + str(item) + '  ')
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # q = Queue()
    z = Queue()

    z.enqueue('1')
    z.enqueue(1)
    z.enqueue('#')
    z.enqueue('sproba')
    print(z.size())
    print(z)
    print(z.get_from_stack('#'))
    print(z)

    '''
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    '''
