"""
>>> q = Queue()
>>> len(q)
0
>>> q.enqueue("aaa")
>>> q.enqueue("bbb")
>>> q.enqueue("ccc")
>>> len(q)
3
>>> q.dequeue()
'aaa'
>>> q.dequeue()
'bbb'
>>> len(q)
1
>>> q.enqueue("ddd")
>>> len(q)
2
>>> q.front()
'ccc'
"""

import math

class Queue:

    def __init__(self, capacity=10):
        # Circular buffer
        self._bf = [None] * capacity

        self._front = 0
        self._back = 0

    def enqueue(self, data):
        self._bf[self._back] = data
        self._back += 1

    def dequeue(self):
        data = self._bf[self._front]
        self._front += 1
        return data

    def __len__(self):
        return abs(self._front - self._back)

    def front(self):
        return self._bf[self._front]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
