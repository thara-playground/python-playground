"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> quick_sort(lx, 0, len(lx) - 1)
>>> lx
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
"""

def quick_sort(a, left, right):
    if left >= right:
        return

    n = len(a)

    i = left
    j = right
    x, y, z = a[i], a[i + (j - i) // 2], a[j]

    if x < y:
        pivot = y if y < z else (x if z < x else z)
    else:
        pivot = y if z < y else (x if x < z else z)

    while True:
        while a[i] < pivot:
            i += 1
        while pivot < a[j]:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    quick_sort(a, left, i - 1)
    quick_sort(a, j + 1, right)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

