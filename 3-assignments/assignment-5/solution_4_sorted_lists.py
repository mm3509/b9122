def merge_sorted_lists(list1, list2):
    """
    >>> merge_sorted_lists([1, 2, 3], [1, 2, 4])
    [1, 1, 2, 2, 3, 4]
    >>> merge_sorted_lists([1, 2, 4], [1, 3, 4])
    [1, 1, 2, 3, 4, 4]
    >>> merge_sorted_lists(123, [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_sorted_lists([1, 2], 123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_sorted_lists([1, "2"], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_sorted_lists([1, 2], [1, "2"])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_sorted_lists([1, 0], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_sorted_lists([1, 2], [1, 0])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    for arg in [list1, list2]:
        assert isinstance(arg, list)
        assert all([isinstance(element, int) for element in arg])
        for i in range(1, len(arg)):
            assert arg[i - 1] <= arg[i]

    new_list = []
    current_index_1 = 0
    current_index_2 = 0

    while True:
        if current_index_1 == len(list1):
            new_list.extend(list2[current_index_2:])
            break

        if current_index_2 == len(list2):
            new_list.extend(list1[current_index_1:])
            break

        element1 = list1[current_index_1]
        element2 = list2[current_index_2]

        if element1 < element2:
            new_list.append(element1)
            current_index_1 += 1
        else:
            new_list.append(element2)
            current_index_2 += 1

    return new_list
