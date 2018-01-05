"""
>>> q = Queue(capacity=5)
>>> len(q)
0
>>> q.enqueue("aaa")
>>> q.enqueue("bbb")
>>> q.enqueue("ccc")
>>> q.enqueue("ddd")
>>> q.enqueue("eee")
>>> len(q)
5
>>> q.enqueue("fff")
Traceback (most recent call last):
...
AssertionError
>>> q.dequeue()
'aaa'
>>> q.dequeue()
'bbb'
>>> len(q)
3
>>> q.enqueue("ggg")
>>> len(q)
4
>>> q.front()
'ccc'
>>> q.dequeue()
'ccc'
"""

import math

class Queue:

    def __init__(self, capacity=10):
        # Circular buffer
        self._bf = [None] * capacity
        self._front = 0
        self._back = 0
        self._capacity = capacity
        self._length = 0

    def enqueue(self, data):
        assert self._length < self._capacity
        self._bf[self._back] = data
        n = self._back + 1
        self._back = 0 if self._capacity <= n else n
        self._length += 1

    def dequeue(self):
        data = self._bf[self._front]
        n = self._front + 1
        self._front = 0 if self._capacity <= n else n
        self._length -= 1
        return data

    def __len__(self):
        return self._length

    def front(self):
        return self._bf[self._front]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
