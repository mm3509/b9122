def remove_all(a_list, item):
    """
    >>> a_list = [1, 2, 3]
    >>> remove_all(a_list, 1)
    >>> a_list
    [2, 3]
    >>> a_list = [1, 2, 3]
    >>> remove_all(a_list, 4)
    >>> a_list
    [1, 2, 3]
    >>> a_list = [2, 2, 3, 4]
    >>> remove_all(a_list, 2)
    >>> a_list
    [3, 4]
    >>> remove_all("abcd", "a_list")
    Traceback (most recent call last):
        ...
    AssertionError
    """

    assert isinstance(a_list, list)

    i = 0
    while i < len(a_list):
        if a_list[i] == item:
            a_list.pop(i)
        i += 1
