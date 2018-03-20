"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> shell_sort(lx)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
"""

def shell_sort(a):
    n = len(a)
    h = n // 2

    while 0 < h:
        i = h
        while i < n:
            t = a[i]
            j = i
            while h <= j and t < a[j - h]:
                a[j] = a[j - h]
                j -= h
            a[j] = t
            i += 1
        h -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
