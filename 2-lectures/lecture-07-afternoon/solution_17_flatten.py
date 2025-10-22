def flatten(some_list):
    """
    >>> flatten([1, 2, [True, False, [1, 2]]])
    [1, 2, True, False, 1, 2]
    >>> flatten([])
    []
    >>> flatten('123')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(some_list, list)

    flattened_list = []

    for element in some_list:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)

    return flattened_list
