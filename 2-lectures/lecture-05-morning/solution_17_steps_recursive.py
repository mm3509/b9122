def count_steps(n):
    """
    >>> count_steps(1)
    1
    >>> count_steps(2)
    2
    >>> count_steps(3)
    3
    >>> count_steps(4)
    5
    >>> count_steps(10)
    89
    """

    # Students: defensive programming only once, here.
    assert isinstance(n, int) and n > 0

    # Students: then we call the inner recursive function, which will
    # not check defensive programming every time.
    return count_steps_rec(n)


def count_steps_rec(n):

    # Students: terminal cases come first.
    if n == 1:
        return 1

    if n == 2:
        return 2

    # Students: then we call the function recursively.
    return count_steps_rec(n - 1) + count_steps(n - 2)
