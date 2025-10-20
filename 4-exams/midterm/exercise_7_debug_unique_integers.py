def find_first_nonunique_integer(i):
    """
    >>> find_first_nonunique_integer(0)
    257
    >>> find_first_nonunique_integer(-6)
    -6
    >>> find_first_nonunique_integer(-5)
    257
    >>> find_first_nonunique_integer("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(i, int)

    while True:

        a = i
        b = i

        if a is b:
            i += 1
            continue

        return i
