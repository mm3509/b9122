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

    # TODO: add defensive programming.

    # TODO: implement the function.
    return


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

    # TODO: add defensive programming.

    # TODO: implement the function.

    return
