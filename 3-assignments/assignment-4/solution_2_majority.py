def majority_element(alist):
    """
    >>> majority_element(["1", "2", "2"])
    '2'
    >>> None is majority_element(["1", "1", "2", "2"])
    True
    >>> majority_element(["1", "1", "2", "2 "])
    '1'
    >>> majority_element(["1", "2", []])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> majority_element(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(alist, list)
    assert all([isinstance(element, str) for element in alist])

    counter = {}
    for element in alist:
        counter[element] = 1 + counter.get(element, 0)

    n = len(alist)
    majority = None
    for element in counter:
        if counter[element] >= n / 2:
            if majority is not None:
                return None
            majority = element

    return majority
