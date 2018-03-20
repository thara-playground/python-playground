
"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> selection_sort(lx)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
"""

def selection_sort(x):
    n = len(x)

    for i in range(n):  # from 0 until n - 1
        min = i
        for j in range(i + 1, n):  # from i + 1 until n - 1
            if x[j] < x[i]:
                min = j
        x[i], x[min] = x[min], x[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
