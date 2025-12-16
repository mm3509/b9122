def merge_lists_keeping_order(list1, list2):
    """
    >>> merge_lists_keeping_order([2, 1, 3], [1, 2, 4])
    [2, 1, 3, 4]
    >>> merge_lists_keeping_order([3], [1, 2, 4])
    [3, 1, 2, 4]
    >>> merge_lists_keeping_order([3, 2], [1, 2, 4])
    [3, 2, 1, 4]
    >>> merge_lists_keeping_order([3, 2, 1], [1, 2, 3])
    [3, 2, 1]
    >>> merge_lists_keeping_order([3, 2, 1], [])
    [3, 2, 1]
    >>> merge_lists_keeping_order([1, 2, 3, 4, 6], [1, 2, 3, 4, 7, 5])
    [1, 2, 3, 4, 6, 7, 5]
    >>> list1 = list(range(10)) + [11]
    >>> list2 = list(range(10)) + [10]
    >>> merge_lists_keeping_order(list1, list2)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    >>> merge_lists_keeping_order([1, "1", 2], [1, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> merge_lists_keeping_order([1, 2, 3], [1, "1", 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> merge_lists_keeping_order([1, 2, 3, 2], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> merge_lists_keeping_order([1, 2, 3], [1, 1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    for arg in [list1, list2]:
        assert isinstance(arg, list)
        assert all([isinstance(i, int) for i in arg])
        assert len(set(arg)) == len(arg)

    # AFA students: this simple solution is correct, but it alters
    # list1 in the argument, i.e. it works "in-place", which is OK
    # for this exercise and for your level.

    # for i in list2:
    #     if i in list1:
    #         list1.append(i)
    #
    # return list1

    # MSFE students: this solution does not alter the original lists. This
    # solution is better practice: changing a list in-place and also returning
    # that list can confuse the user and lead to bugs.

    new_regions = list2.copy()
    for i in list1:
        if i not in new_regions:
            continue
        new_regions.remove(i)

    return list1 + new_regions
