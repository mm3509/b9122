def helper_value_of_list_at(alist, i):
    try:
        return alist[i]
    except IndexError:
        return None


def find_first_nonzero_element(alist):
    """
    >>> find_first_nonzero_element([])
    -1
    >>> find_first_nonzero_element([0, 0, 0, 1, 2, 3])
    3
    >>> find_first_nonzero_element(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(alist, list)

    i = 0
    while True:
        value = helper_value_of_list_at(alist, i)
        if value == 0:
            i += 1
            continue
        if value is None:
            return -1
        return i


def find_first_nonzero_element_fast(alist):
    """
    >>> find_first_nonzero_element_fast([])
    -1
    >>> find_first_nonzero_element_fast([0] * int(1e5) + [1, 2, 3])
    100000
    >>> find_first_nonzero_element_fast(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(alist, list)

    index_human = 1  # Start at 1 so that *= 2 works at the beginning.

    # These are the right initial values so the fast algorithm works on the
    # empty list.
    lower_bound = -2
    upper_bound = -1
    while True:
        value = helper_value_of_list_at(alist, index_human - 1)
        if value == 0:
            lower_bound = index_human - 1
            index_human *= 2
            continue

        if lower_bound != upper_bound - 1:
            upper_bound = index_human - 1
            index_human = 1 + (upper_bound + lower_bound) // 2
            continue

        return lower_bound + 1
