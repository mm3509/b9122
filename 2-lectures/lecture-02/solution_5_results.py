def is_leap_year(n):
    """
    >>> is_leap_year(1984)
    True
    >>> is_leap_year(1985)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year('1984')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    >>> is_leap_year(1984.0)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    >>> is_leap_year(-4)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    >>> is_leap_year(0)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    """

    if not (isinstance(n, int) and n > 0):
        raise ValueError("argument must be a positive integer")

    if n % 400 == 0:
        return True

    if n % 100 == 0:
        return False

    if n % 4 == 0:
        return True

    return False
