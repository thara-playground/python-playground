"""
>>> t = BinaryTree()
>>> t.set_root(10)
>>> t.insert_left(20)
>>> t.insert_right(15)
>>> t.root()
10
>>> t.list_by_pre_order()
[10, 20, 15]
>>> t.list_by_post_order()
[20, 15, 10]
>>> t.list_by_in_order()
[20, 10, 15]
>>> t.list_by_breadth_first()
[10, 20, 15]
>>> t.get_left().insert_left(210)
>>> t.get_left().insert_right(220)
>>> t.get_right().insert_left(160)
>>> t.get_right().insert_right(170)
>>> t.list_by_pre_order()
[10, 20, 210, 220, 15, 160, 170]
>>> t.list_by_post_order()
[210, 220, 20, 160, 170, 15, 10]
>>> t.list_by_in_order()
[210, 20, 220, 10, 160, 15, 170]
>>> t.list_by_breadth_first()
[10, 20, 15, 210, 220, 160, 170]
"""
from queue import Queue

class Node:
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None

    def root(self):
        return self._value

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def set_root(self, value):
        self._value = value

    def insert_left(self, value):
        self._left = Node()
        self._left.set_root(value)

    def insert_right(self, value):
        self._right = Node()
        self._right.set_root(value)

    def list_by_pre_order(self):
        values = [self._value]
        if self._left is not None:
            values.extend(self._left.list_by_pre_order())
        if self._right is not None:
            values.extend(self._right.list_by_pre_order())
        return values

    def list_by_post_order(self):
        values = []
        if self._left is not None:
            values.extend(self._left.list_by_post_order())
        if self._right is not None:
            values.extend(self._right.list_by_post_order())
        values.append(self._value)
        return values

    def list_by_in_order(self):
        values = []
        if self._left is not None:
            values.extend(self._left.list_by_in_order())
        values.append(self._value)
        if self._right is not None:
            values.extend(self._right.list_by_in_order())
        return values

    def list_by_breadth_first(self):
        values = []

        q = Queue()
        q.enqueue(self)
        while len(q) != 0:
            o = q.dequeue()
            values.append(o.root())
            if o._left is not None:
                q.enqueue(o._left)
            if o._right is not None:
                q.enqueue(o._right)
        return values



BinaryTree = Node


if __name__ == "__main__":
    import doctest
    doctest.testmod()
