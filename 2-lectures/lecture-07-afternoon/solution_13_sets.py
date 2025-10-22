def list_has_only_unique_integers(a_list):
    """
    >>> list_has_only_unique_integers([1, 2, 3])
    True
    >>> list_has_only_unique_integers([1, 1, 2])
    False
    >>> list_has_only_unique_integers(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> list_has_only_unique_integers([1, "1"])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(a_list, list)
    assert all([isinstance(i, int) for i in a_list])

    return len(set(a_list)) == len(a_list)
