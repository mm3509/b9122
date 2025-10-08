def square(x):
    return x ** 2


def compute_integral(fn, start, end, step):
    """
    >>> compute_integral(square, 0, 1, 0.2)
    0.33
    >>> compute_integral('abcd', 0, 1, 0.1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> compute_integral(square, 'abcd', 1, 0.1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> compute_integral(square, 0, 'abcd', 0.1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> compute_integral(square, 0, 1, 'abcd')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> compute_integral(square, 0, 1, 1.1)
    Traceback (most recent call last):
    ...
    AssertionError
    """


    # TODO: add defensive programming.


    # TODO: implement the function.

    return
