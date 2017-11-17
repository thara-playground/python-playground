"""
>>> LinkedList = DoublyLinkedList
>>> l = LinkedList()
>>> len(l)
0
>>> l = LinkedList(1, 2, 3)
>>> len(l)
3
>>> l = LinkedList(12, 99, 37)
>>> for e in l:
...     print(e)
12
99
37
>>> l.append(37)
>>> len(l)
4
>>> l[0]
12
>>> l[2]
37
>>> l[4]
Traceback (most recent call last):
...
IndexError: Not found
>>> 
>>> l = LinkedList(12,99,37)
>>> l.insert(0, 128)
>>> l.insert(2, 256)
>>> l[0], l[1], l[2], l[3]
(128, 12, 256, 99)
>>> l.insert(5, 1024)
>>> l[4], l[5]
(37, 1024)
>>> len(l)
6
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self, *args):
        self._dummy = Node(None)
        self._dummy.prev = self._dummy
        self._dummy.next = self._dummy
        self._first = self._dummy.next
        self._last = self._dummy.prev

        current = self._first
        for v in args:
            new_node = Node(v)
            current.next = new_node
            new_node.prev = current
            current = new_node
        current.next = self._dummy
        self._dummy.prev = current

    def append(self, value):
        new_node = Node(value)
        self._last.prev.next = new_node
        new_node.prev = self._last.prev
        new_node.next = self._dummy
        self._last.prev = new_node

    def __iter__(self):
        current = self._first.next
        while True:
            if current == self._dummy:
                raise StopIteration()
            yield current.value
            current = current.next

    def __len__(self):
        return sum(1 for _ in self)

    def __getitem__(self, index):
        for i, e in enumerate(self):
            if i == index:
                return e
        raise IndexError("Not found")

    def insert(self, index, value):
        new_node = Node(value)

        size = len(self)

        if index <= (size / 2):
            i = 0
            current = self._first.next
            while i <= size:
                if i == index:
                    prev = current.prev
                    prev.next = new_node
                    current.prev = new_node
                    new_node.prev = prev
                    new_node.next = current
                    break
                else:
                    current = current.next
                i = i + 1
        else:
            i = size
            current = self._last
            while 0 <= i:
                if i == index:
                    prev = current.prev
                    prev.next = new_node
                    current.prev = new_node
                    new_node.prev = prev
                    new_node.next = current
                    break
                else:
                    current = current.prev
                i = i - 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
