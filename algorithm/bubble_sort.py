"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> bubble_sort(lx)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
"""

def bubble_sort(x):
    i = 0
    n = len(x)

    while True:
        swapped = False
        for i in range(1, n):  # from 1 until n -1
            a, b = x[i-1], x[i]
            if a > b:
                x[i-1], x[i] = b, a
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    import doctest
    doctest.testmod()
