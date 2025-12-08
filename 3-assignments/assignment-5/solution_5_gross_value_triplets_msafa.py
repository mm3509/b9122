def verify_argument(alist):

    assert isinstance(alist, list)
    assert all([isinstance(element, int) for element in alist])


def __partial_sum(alist, i, j):

    if i == j:
        return 0

    if j >= len(alist):
        return sum(alist[i:])

    return sum(alist[i:j])


def __gross_value(alist, i, j, k):

    n = len(alist)
    return (__partial_sum(alist, 0, i)
            - __partial_sum(alist, i, j)
            + __partial_sum(alist, j, k)
            - __partial_sum(alist, k, n + 1))


def find_triplets(alist):
    """
    >>> find_triplets([-5, 3, 9, 4])
    21
    >>> find_triplets(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_triplets([1, "2", 3])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    verify_argument(alist)

    n = len(alist)
    maximum = sum(alist)

    for i in range(n):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                value = __gross_value(alist, i, j, k)

                if value >= maximum:
                    maximum = value

    return maximum
