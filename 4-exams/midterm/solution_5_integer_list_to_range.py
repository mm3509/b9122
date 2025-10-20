def helper_range(start, end):
    """
    >>> helper_range(1, 1)
    '1'
    >>> helper_range(1, 2)
    '1-2'
    """

    if start == end:
        return str(start)

    return str(start) + "-" + str(end)


def format_ranges(alist):
    """
    >>> format_ranges([1, 2, 3])
    '1-3'
    >>> format_ranges([1, 2, 4, 5, 7])
    '1-2,4-5,7'
    >>> format_ranges([7, 2, 4, 5, 1])
    '1-2,4-5,7'
    >>> format_ranges([])
    ''
    >>> format_ranges([1, 1])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> format_ranges(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> format_ranges([1, "1"])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(alist, list)
    assert all([isinstance(i, int) for i in alist])
    assert len(set(alist)) == len(alist)

    if [] == alist:  # Alternatively: if not alist:
        return ''

    sorted_list = sorted(alist)
    smallest = sorted_list[0]

    start = smallest
    current_end = smallest
    formatted_range = []

    for i in sorted_list[1:]:

        if i == current_end + 1:
            current_end = i
            continue

        formatted_range.append(helper_range(start, current_end))

        start = i
        current_end = i

    formatted_range.append(helper_range(start, current_end))

    return ",".join(formatted_range)
