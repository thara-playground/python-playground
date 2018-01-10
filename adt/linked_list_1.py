"""
>>> LinkedList = SinglyLinkedList
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
>>> del l[3]
>>> l[0], l[1], l[2], l[3], l[4]
(128, 12, 256, 37, 1024)
>>> del l[0]
>>> del l[3]
>>> l[0], l[1], l[2]
(12, 256, 37)
>>> len(l)
3
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, *args):
        if 0 < len(args):
            self._first = Node(args[0])
            current = self._first
            for e in args[1:]:
                new_node = Node(e)
                current.next = new_node
                current = new_node
        else:
            self._first = None

    def append(self, value):
        new_node = Node(value)
        if self._first is None:
            self._first = new_node
        else:
            current = self._first
            while current.next is not None:
                current = current.next
            current.next = new_node

    def __iter__(self):
        current = self._first
        while True:
            if current is None:
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
        prev = None
        current = self._first
        i = 0
        new_node = Node(value)

        size = len(self)
        while i <= size:
            if i == index:
                if prev is None:
                    new_node.next = self._first
                    self._first = new_node
                else:
                    new_node.next = current
                    prev.next = new_node
                break
            else:
                prev = current
                current = current.next
            i = i + 1

    def __delitem__(self, index):

        if index == 0:
            self._first = self._first.next
            return

        prev = None
        next = None

        i = 0
        size = len(self)
        current = self._first
        while current is not None:
            if i == index:
                next = current.next
                break
            prev = current
            current = current.next
            i = i + 1

        if prev is None:
            pass

        if prev is None and next is None:
            raise IndexError("Not found")
        prev.next = next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
