"""
>>> h = HashTable()
>>> len(h)
0
>>> h["k1"] = "aaa"
>>> h["k2"] = "bbb"
>>> h["k3"] = "ccc"
>>> len(h)
3
>>> h["k1"]
'aaa'
>>> h["k2"]
'bbb'
>>> h["k4"]
Traceback (most recent call last):
...
AttributeError: Not found
>>> del h["k2"]
>>> len(h)
2
>>> del h["k2"]
Traceback (most recent call last):
...
AttributeError: Not found
"""
from linked_list_1 import SinglyLinkedList as LinkedList


class Bucket:

    def __init__(self):
        self._entries = LinkedList()
        self._empty = True

    @property
    def is_empty(self):
        return self._empty

    def __getitem__(self, key):
        for k, v in self._entries:
            if k == key:
                return v
        return None

    def append(self, key, value):
        self._entries.append((key, value))
        self._empty = False

    def delete(self, key):
        n = -1
        for n, (k, _) in enumerate(self._entries):
            if k == key:
                break
        del self._entries[n]

        if len(self._entries) == 0:
            self._empty = True

    def __len__(self):
        return len(self._entries)


# Use Separate chaining
class HashTable:

    def __init__(self, size=10):
        self._table_size = size
        self._hash_func = hash
        self._table = [Bucket() for _ in range(size)]

    def __getitem__(self, key):
        h = self._hash(key)
        value = self._table[h][key]
        if value is None:
            raise AttributeError("Not found")
        return value

    def __setitem__(self, key, value):
        h = self._hash(key)
        self._table[h].append(key, value)

    def __delitem__(self, key):
        h = self._hash(key)
        value = self._table[h][key]
        if value is None:
            raise AttributeError("Not found")
        self._table[h].delete(key)

    def _hash(self, key):
        return self._hash_func(key) % self._table_size

    def __len__(self):
        n = 0
        for b in self._table:
            if not b.is_empty:
                n += len(b)
        return n

if __name__ == "__main__":
    import doctest
    doctest.testmod()
