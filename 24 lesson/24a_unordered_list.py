'''
Task 1. Extend UnorderedList
Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.
'''


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):  # использует уже определённую add
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self._head
        while current is not None:
            temp_list.add(current.get_data())
            current = current.get_next()
        temp_list.add(item)
        current = temp_list._head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def pop(self):  # без использования remove
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self._head
        while current is not None:
            temp_list.add(current.get_data())
            current = current.get_next()
        current = temp_list._head
        i = 0
        while current is not None:
            if i == 0:
                result = current.get_data()
                current = current.get_next()
                i = 1
            new_list.add(current.get_data())
            current = current.get_next()
        return result, new_list

    '''
    # с использованием [https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/]
    def pop(self):
        if self.is_empty():
            return None
        else:
            # Removes the head node and makes
            # the preceeding one the new head
            poppednode = self._head
            temp = Node(poppednode)
            temp.set_next(self._head)
            self._head = temp
            poppednode.next = None
            return poppednode._data
    '''

    def index(self, num):
        i = 0
        current = self._head
        while current is not None:
            if i == num:
                return current.get_data()
            else:
                i += 1
                current = current.get_next()
        else:
            return 'Out of range!'

    def insert(self, num, item):
        i = 0
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self._head
        if num == self.size():  # используется уже определённая size
            return self.append(item)  # используется уже определённый append
        while current is not None:
            if i == num:
                temp_list.add(item)
            temp_list.add(current.get_data())
            current = current.get_next()
            i += 1
        current = temp_list._head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def slice_stack(self, start, stop):
        i = 0
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self._head
        while current is not None:
            if start <= i < stop:
                temp_list.add(current.get_data())
                current = current.get_next()
                i += 1
            else:
                current = current.get_next()
                i += 1
        current = temp_list._head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += ' ' + str(current.get_data())
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    # print(my_list.append(00))
    print(my_list.pop())
    # print(my_list.index(0))
    # print(my_list.index(2))
    # print(my_list.index(7))
    # print(my_list.insert(3, 101))
    # print(my_list.insert(6, 201))
    # print(my_list.slice_stack(1, 3))

    '''
    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    '''
