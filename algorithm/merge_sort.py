"""
>>> lx = [8, 4, 3, 7, 6, 5, 2, 1]
>>> merge_sort(lx)
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
"""

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a

    m = n // 2
    left, right = a[:m], a[m:]
#     left = list()
#     right = list()
#     i = 0
#     while i < n:
#         if i < (n // 2):
#             left.append(a[i])
#         else:
#             right.append(a[i])
#         i += 1

    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(list(left), list(right))


def _merge(left, right):
    result = list()

    while 0 < len(left) and 0 < len(right):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while 0 < len(left):
        result.append(left[0])
        left = left[1:]
    while 0 < len(right):
        result.append(right[0])
        right = right[1:]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

