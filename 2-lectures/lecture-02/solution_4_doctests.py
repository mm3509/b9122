# From Miguel: ignore lines with "doctest" for now.
import doctest


def compute_interest(principal, rate, periods):
    """
    >>> a = compute_interest(100, 0.05, 1)
    >>> int(a)
    5
    >>> b = compute_interest(100, 0.05, 10)
    >>> int(b)
    62
    >>> compute_interest("100", 0.05, 10)
    Traceback (most recent call last):
    ...
    TypeError: argument must be ...
    >>> compute_interest(100, [], 10)
    Traceback (most recent call last):
    ...
    TypeError: argument must be ...
    >>> compute_interest(100, 0.05, {})
    Traceback (most recent call last):
    ...
    TypeError: argument must be ...
    >>> compute_interest(-100, 0.05, 1)
    Traceback (most recent call last):
    ...
    ValueError: argument must be ...
    >>> compute_interest(-100, -0.05, 1)
    Traceback (most recent call last):
    ...
    ValueError: argument must be ...
    >>> compute_interest(100, 0.05, -1)
    Traceback (most recent call last):
    ...
    ValueError: argument must be ...
    >>> compute_interest(0, 0.05, 1)
    0.0
    >>> compute_interest(100, 0, 1)
    0
    >>> compute_interest(100, 0.05, 0)
    0.0
    """

    for arg in [principal, rate, periods]:
        if not isinstance(arg, (int, float)):
            raise TypeError("argument must be a number")
        if arg < 0:
            raise ValueError("argument must be positive")
    
    return principal * (1 + rate) ** periods - principal


if "__main__" == __name__:
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 < tests_run:
        assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
        print('Your doc-tests pass, congratulations!')
    else:
        print('Unable to run doc-tests, please see Miguel!')
