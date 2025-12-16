def generate_log_range(leading, orders_magnitude):
    """
    >>> generate_log_range([1, 2, 5], [0, 2])
    [1, 2, 5, 10, 20, 50, 100, 200, 500]
    >>> generate_log_range([1, 5], [0, 2])
    [1, 5, 10, 50, 100, 500]
    >>> generate_log_range([1, 2, 5], [0, 1])
    [1, 2, 5, 10, 20, 50]
    >>> generate_log_range([6, 3], [2, 0])
    [3, 6, 30, 60, 300, 600]
    >>> generate_log_range([1, 5], [3, 1])
    [10, 50, 100, 500, 1000, 5000]
    >>> generate_log_range([1, 5], [2, 2])
    [100, 500]
    >>> generate_log_range("abc", [1, 3])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 2], "abc")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range(["abc"], [1, 3])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 2], ["abc"])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 1, 2], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 2], [1, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([0, 1], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 10], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([-1, 5], [1, 0])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_log_range([1, 5], [-1, 0])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    for arg in [leading, orders_magnitude]:
        assert isinstance(arg, list)
        assert all([isinstance(element, int) for element in arg])

    assert len(set(leading)) == len(leading)
    assert 2 == len(orders_magnitude)
    assert all([1 <= element <= 9 for element in leading])
    assert all([element >= 0 for element in orders_magnitude])

    order_start = min(orders_magnitude)
    order_end = max(orders_magnitude)

    log_range = []
    for j in range(order_start, order_end + 1):
        for i in sorted(leading):
            log_range.append(i * 10 ** j)

    return log_range
