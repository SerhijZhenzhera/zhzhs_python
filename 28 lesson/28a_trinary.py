'''
Task 1
Implement a binary heap as a max heap -> trinary
'''

import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return (pos + 1) // 3

    def leftChild(self, pos):
        return (3 * pos) - 1

    def centralChild(self, pos):
        return 3 * pos

    def rightChild(self, pos):
        return (3 * pos) + 1

    def isLeaf(self, pos):
        if pos >= ((self.size+1)//3) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.centralChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                if (self.Heap[self.leftChild(pos)] > self.Heap[self.centralChild(pos)] and self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                elif (self.Heap[self.centralChild(pos)] > self.Heap[self.leftChild(pos)] and self.Heap[self.centralChild(pos)] > self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.centralChild(pos))
                    self.maxHeapify(self.centralChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size // 3) + 2):
            print(" PARENT: " + str(self.Heap[i]) + ", LEFT CHILD: " + str(
                self.Heap[3 * i - 1]) + ", CENTRAL CHILD: " + str(
                self.Heap[3 * i]) + ", RIGHT CHILD: " + str(self.Heap[3 * i + 1]))

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


if __name__ == '__main__':

    print('The maxHeap is ')

    maxHeap = MaxHeap(30)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)
    maxHeap.insert(7)
    maxHeap.insert(1)
    maxHeap.insert(2)
    maxHeap.insert(11)
    maxHeap.insert(13)

    maxHeap.Print()

    print("The Max val is " + str(maxHeap.extractMax()))


'''
---output---
The maxHeap is
 PARENT: 84, LEFT CHILD: 19, CENTRAL CHILD: 22, RIGHT CHILD: 11
 PARENT: 19, LEFT CHILD: 13, CENTRAL CHILD: 17, RIGHT CHILD: 6
 PARENT: 22, LEFT CHILD: 5, CENTRAL CHILD: 9, RIGHT CHILD: 7
 PARENT: 11, LEFT CHILD: 1, CENTRAL CHILD: 2, RIGHT CHILD: 10
 PARENT: 13, LEFT CHILD: 3, CENTRAL CHILD: 0, RIGHT CHILD: 0
The Max val is 84
'''
