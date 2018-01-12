"""
>>> t = BinarySearchTree(8)
>>> t.insert(10)
>>> t.insert(14)
>>> t.insert(4)
>>> t.insert(1)
>>> t.insert(13)
>>> t.insert(6)
>>> t.insert(7)
>>> t.insert(3)
>>> t.to_list()
[1, 3, 4, 6, 7, 8, 10, 13, 14]
>>> 7 in t
True
>>> 5 in t
False
>>> t2 = t.remove(6)
>>> t.to_list()
[1, 3, 4, 7, 8, 10, 13, 14]
>>> t3 = t.remove(8)
>>> t3.to_list()
[1, 3, 4, 7, 10, 13, 14]
>>> t3.value
10
"""


class Node:

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    def insert(self, item):
        if self._value == item:
            return
        elif item < self._value:
            if self._left is None:
                self._left = Node(item)
            else:
                return self._left.insert(item)
        elif self._value < item:
            if self._right is None:
                self._right = Node(item)
            else:
                return self._right.insert(item)

    def __contains__(self, item):
        if self._value == item:
            return True
        elif item < self._value:
            if self._left is None:
                return False
            return item in self._left
        elif self._value < item:
            if self._right is None:
                return False
            return item in self._right

    def to_list(self):
        values = []
        if self._left is not None:
            values.extend(self._left.to_list())
        values.append(self._value)
        if self._right is not None:
            values.extend(self._right.to_list())
        return values

    def remove(self, item):
        if self._value == item:
            if self._left is None:
                return self._right
            elif self._right is None:
                return self._left
            n = self._right._min_node()
            self._value = n._value
            self._right = self._right.remove(n._value)
        elif item < self._value:
            self._left = self._left.remove(item)
        elif self._value < item:
            self._right = self._right.remove(item)
        return self

    def _min_node(self):
        if self._left is None:
            return self
        return _min_node(self._left)


BinarySearchTree = Node

if __name__ == "__main__":
    import doctest
    doctest.testmod()


