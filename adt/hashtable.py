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

class Bucket:

    def __init__(self):
        self._empty = True
        self._deleted = False
        self._key = None
        self._value = None

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def is_empty(self):
        return self._empty

    @property
    def is_deleted(self):
        return self._deleted

    def fill(self, key, value):
        self._key = key
        self._value = value
        self._empty = False

    def delete(self):
        self._key = None
        self._value = None
        self._deleted = True

# Use Open addressing
class HashTable:

    def __init__(self, size=10):
        self._table_size = size
        self._hash_func = hash
        self._table = [Bucket() for _ in range(size)]

    def __getitem__(self, key):
        h = self._hash(key)
        while not self._table[h].is_empty:
            b = self._table[h]
            if not b.is_deleted and b.key == key:
                return b.value
            h = self._rehash(h)
        raise AttributeError("Not found")

    def __setitem__(self, key, value):
        h = self._hash(key)
        # Search empty bucket
        while not self._table[h].is_empty:
            h = self._rehash(h)
        self._table[h].fill(key, value)

    def __delitem__(self, key):
        h = self._hash(key)
        while not self._table[h].is_empty:
            b = self._table[h]
            if b.key == key:
                b.delete()
                return
            h = self._rehash(h)
        raise AttributeError("Not found")

    def _hash(self, key):
        return self._hash_func(key) % self._table_size

    def _rehash(self, hash_value):
        return (hash_value + 1) % self._table_size

    def __len__(self):
        n = 0
        for b in self._table:
            if not b.is_empty and not b.is_deleted:
                n += 1
        return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
