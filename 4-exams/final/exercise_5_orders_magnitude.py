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
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return
