"""
>>> lx = [1,3,5,11,12,13,17,22,25,28]
>>> binary_search(lx, 0)
>>> binary_search(lx, 1)
0
>>> binary_search(lx, 3)
1
>>> binary_search(lx, 13)
5
>>> binary_search(lx, 25)
8
>>> binary_search(lx, 28)
9
"""

def binary_search(a, test):
    l = 0
    r = len(a) - 1

    while l <= r:
        m = (l + r) // 2
        if a[m] < test:
            l = m + 1
        elif a[m] > test:
            r = m - 1
        else:
            return m
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
