"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> insertion_sort(lx)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> insertion_sort_recursive(lx)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
"""

def insertion_sort(a):
    i = 1
    n = len(a)

    while i < n:
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        i += 1

    # while i < n:
    #     j = i
    #     while j > 0 and a[j - 1] > a[j]:
    #         a[j], a[j - 1] = a[j - 1], a[j]
    #         j -= 1
    #     i += 1


def insertion_sort_recursive(a, n=None):
    if n is None:
        n = len(a) - 1

    if 0 < n:
        insertion_sort_recursive(a, n - 1)
        x = a[n]
        j = n - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
