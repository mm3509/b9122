def get_unique(alist):
    """
    >>> get_unique([2, 2, 4, 4, 6, 8, 9, 10, 10])
    [2, 4, 6, 8, 9, 10]
    >>> get_unique([2, 4, 6, 8, -9, 10])
    [-9, 2, 4, 6, 8, 10]
    >>> get_unique(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> get_unique([2.5, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(alist, list)
    assert all([isinstance(i, int) for i in alist])

    # Solution with a for loop:
    
    # unique_list = []
    # for element in alist:
    #     if element in unique_list:
    #         continue
    #     unique_list.append(element)
    # 
    # return sorted(unique_list)
    
    # Solution with sets:
    return sorted(set(alist))
