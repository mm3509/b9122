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

        # `a = i` just copies the reference, so it will always be the
        # same address. To force a change of memory address, you have
        # to manipulate an immutable. For example, add and subtract 1
        # or 2, which forces the creation of a new integer (integers
        # are immutable). Or convert to a string first, then to an
        # integer. Strings are immutable, so the `int()` function has
        # to return a new value (in addition to returning a different
        # type), which will be at a different memory address from `i`.

        # A comment like this one is enough to prevent reintroduction
        # of the bug when refactoring.

        # Manipulate the immutable to force the creation of a new copy, at a
        # different memory address.
        a = int(str(i))  # Or: i + 1 - 1
        b = int(str(i))  # Or: i + 2 - 2

        if a is b:
            i += 1
            continue

        return i
