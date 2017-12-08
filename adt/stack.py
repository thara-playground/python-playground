"""
>>> s = Stack()
>>> len(s)
0
>>> s.push("aaa")
>>> s.push("bbb")
>>> s.push("ccc")
>>> len(s)
3
>>> s.pop()
'ccc'
>>> s.pop()
'bbb'
>>> len(s)
1
>>> s.push("ddd")
>>> len(s)
2
>>> s.peek()
'ddd'
"""

class Stack:

    def __init__(self, capacity=10):
        self._data = [None] * 10
        self._length = 0
        self._capacity = capacity

    def __len__(self):
        return self._length

    def push(self, value):
        l = self._length + 1
        assert l < self._capacity
        self._data[l] = value
        self._length = l

    def pop(self):
        value = self._data[self._length]
        self._length -= 1
        return value

    def peek(self):
        return self._data[self._length]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
