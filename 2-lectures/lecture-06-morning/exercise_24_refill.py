SEPARATOR = " "


def refill_rec(s, max_chars):

    # TODO: implement this function, without defensive programming.
    return


def refill(s, max_chars=80):
    """
    >>> refill('')
    []
    >>> refill('abcd', max_chars=2)
    ['ab', 'cd']
    >>> refill('abc', max_chars=2)
    ['ab', 'c']
    >>> refill('1234567', max_chars=3)
    ['123', '456', '7']
    >>> refill('123456789', max_chars=2)
    ['12', '34', '56', '78', '9']
    >>> refill('abcd', max_chars=3)
    ['abc', 'd']
    >>> refill('ab cd ef gh', max_chars=5)
    ['ab cd', 'ef gh']
    >>> refill('I will send an announcement', max_chars=15)
    ['I will send an', 'announcement']
    >>> refill(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> refill('abcd', '80')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # TODO: implement defensive programing.

    # TODO: call the recursive helper function.
