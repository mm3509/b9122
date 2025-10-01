def factorial(n):
    """
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    # Students: this wrapper function handles defensive programming,
    # then calls the inner recursive function without these checks.
    assert isinstance(n, int) and n >= 0

    return factorial_rec(n)


def factorial_rec(n):
    # Students: This inner recursive function avoids checking
    # defensive programming n times.

    # Students: handle the terminal case first.
    if n == 0:
        return 1

    # Students: then call itself.
    return n * factorial_rec(n - 1)
