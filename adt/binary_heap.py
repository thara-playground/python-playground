"""
>>> t = BinaryHeap()
>>> t.append(11)
>>> t.append(3)
>>> t.append(5)
>>> t.append(8)
>>> t.append(4)
>>> t.append(15)
>>> t.in_order()
[3, 8, 4, 15, 5, 11]
"""


class BinaryHeap:

    def __init__(self, capacity=50):
        self._data = [None] * (capacity + 1)
        self._bottom = 1

    def _len(self):
        return len(self._data) - 1

    def append(self, value):
        self._data[self._bottom] = value
        self._bublle_up(self._bottom)
        self._bottom += 1

    def _bublle_up(self, n):
        parent = n // 2
        if self._data[parent] is None:
            return
        if self._data[parent] < self._data[n]:
            x, y = self._data[n], self._data[parent]
            self._data[n], self._data[parent] = y, x
            self._bublle_up(parent)

    def remove(self, value):
        if self._data[1] == value:  # Remove root
            self.data[1], self.data[self._bottom] = self.data[self._bottom], self.data[1]
            self._bottom -= 1
            _bublle_down(1)
        else:
            pass

    def _bublle_down(self, n):
        if self._bottom < n:
            return
        for i in [1, 0]:
            child = 2 * n + i
            if self._data[n] < self._data[child]:
                x, y = self._data[n], self._data[child]
                self._data[n], self._data[child] = y, x
                self._bublle_down(child)
        # WIP




    def in_order(self):
        return self._in_order(1)

    def _in_order(self, n):
        if self._len() < n or self._data[n] is None:
            return []
        return self._in_order(n * 2) + [self._data[n]] + self._in_order(n * 2 + 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
