def factorial(n):
    """
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """

    assert isinstance(n, int) and n >= 0

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
