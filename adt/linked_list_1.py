
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    >>> l = SinglyLinkedList()
    >>> len(l)
    0
    >>> l = SinglyLinkedList(1)
    >>> len(l)
    1
    >>> l = SinglyLinkedList(1, 2, 3)
    >>> len(l)
    3
    """

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
        """
        >>> l = SinglyLinkedList(12, 99, 37)
        >>> for e in l:
        ...     print(e)
        12
        99
        37
        """
        current = self._first
        while True:
            if current is None:
                raise StopIteration()
            yield current.value
            current = current.next

    def __len__(self):
        """
        >>> l = SinglyLinkedList()
        >>> len(l)
        0
        >>> l = SinglyLinkedList(12, 99)
        >>> len(l)
        2
        >>> l.append(37)
        >>> len(l)
        3
        """
        return sum(1 for _ in self)

    def __getitem__(self, index):
        """
        >>> l = SinglyLinkedList(12,99,37)
        >>> l[0]
        12
        >>> l[2]
        37
        >>> l[3]
        Traceback (most recent call last):
        ...
        IndexError: Not found
        """
        for i, e in enumerate(self):
            if i == index:
                return e
        raise IndexError("Not found")

    def insert(self, index, value):
        """
        >>> l = SinglyLinkedList(12,99,37)
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
