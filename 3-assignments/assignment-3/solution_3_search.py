def verify_argument(alist):
    assert isinstance(alist, list)
    assert all([isinstance(a, int) for a in alist])
    assert 1 <= len(alist)


def find_min_and_max(alist):
    """
    >>> find_min_and_max([1])
    (1, 1)
    >>> find_min_and_max([1, 5, 10, 50, 100])
    (1, 100)
    >>> find_min_and_max([])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_min_and_max([123, "abc"])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    verify_argument(alist)

    smallest = alist[0]
    largest = alist[0]

    for i in alist[1:]:
        if i < smallest:
            smallest = i
            continue
        if largest < i:
            largest = i

    # Students: this is how you can return a tuple with two elements: just add
    # a comma between them
    return smallest, largest


def find_min_and_max_fast(alist):
    """
    >>> find_min_and_max_fast([1])
    (1, 1)
    >>> find_min_and_max_fast([1, 5, 10, 50, 100])
    (1, 100)
    >>> find_min_and_max_fast([])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_min_and_max_fast([123, "abc"])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    verify_argument(alist)

    if 1 == len(alist):
        return alist[0], alist[0]

    smaller = []
    larger = []

    # In case the list has an odd number,
    # save the first element and skip it
    if 1 == len(alist) % 2:
        smaller.append(alist[0])
        larger.append(alist[0])

    current_index = len(alist) % 2
    for _ in range(len(alist) // 2):
        element1 = alist[current_index]
        element2 = alist[current_index + 1]
        current_index += 2

        if element1 < element2:
            smaller.append(element1)
            larger.append(element2)
            continue

        larger.append(element1)
        smaller.append(element2)

    # TODO: understand why the recursive solution does not benefit from this
    # improvement.

    # Students: you could then search recursively, calling the
    # lines below, but for lists larger than

    # smallest, _ = find_min_and_max_fast_rec(smaller)
    # _, largest = find_min_and_max_fast_rec(larger)
    #
    # return smallest, largest

    smallest = smaller[0]
    for i in smaller[1:]:
        if i < smallest:
            smallest = i

    largest = larger[0]
    for i in larger[1:]:
        if largest < i:
            largest = i

    return smallest, largest
