def count_syllabifications(n):
    """
    >>> count_syllabifications(1)
    1
    >>> count_syllabifications(2)
    2
    >>> count_syllabifications(3)
    4
    >>> count_syllabifications(4)
    7
    >>> count_syllabifications(5)
    13
    >>> count_syllabifications(6)
    24
    >>> count_syllabifications(0)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_syllabifications(-1)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_syllabifications("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(n, int) and n >= 1

    # Students: alternative to recursion, which is faster.
    # alist = [1, 2, 4]
    # for i in range(n - 3):
    #     alist.append(sum(alist[-3:]))
    # return alist[n - 1]

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    # Students: any arrangement starts with either a short syllable (and the
    # number of those arrangements is: count_syllabifications(n-1)), a medium
    # sylalble (with count_syllabifications(n - 2) arrangements) or a long
    # syllable (with count_syllabifications(n - 3) arrangements). It's similar
    # to counting steps and the Fibonacci sequence.
    total = (count_syllabifications(n - 1)
             + count_syllabifications(n - 2)
             + count_syllabifications(n - 3))

    return total
