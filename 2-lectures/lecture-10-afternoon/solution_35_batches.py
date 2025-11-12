MAX_ITEMS = 5


def make_batches(alist):
    """
    >>> make_batches([1, 2, 3, 4, 5, 6, 7])
    [[1, 2, 3, 4, 5, 6, 7]]
    >>> make_batches([1, 2, 3, 4, 5, 6, 7, 8])
    [[1, 2, 3, 4, 5], [6, 7, 8]]
    >>> make_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
    >>> make_batches([])
    [[]]
    >>> make_batches([1, 1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> make_batches(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> make_batches([1, 2, "3"])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(alist, list)
    assert all([isinstance(num, int) for num in alist])
    assert len(set(alist)) == len(alist)
    
    # Recursive programming:

    if len(alist) <= 1.5 * MAX_ITEMS:
        return [alist]
    
    return [alist[:MAX_ITEMS]] + make_batches(alist[MAX_ITEMS:])


    # Imperative programming version:

    # if alist == []:
    #     return [[]]
    # 
    # batches = []
    # while alist:
    #     if len(alist) <= MAX_ITEMS * 1.5:
    #         batches.append(alist)
    #         break
    #     next_batch = []
    #     for _ in range(MAX_ITEMS):
    #         next_batch.append(alist.pop(0))
    #     batches.append(next_batch)
    # 
    # return batches
