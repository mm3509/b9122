DAYS_IN_YEAR = 250


def annualize_return(interest_rate):
    """
    >>> annualize_return(0.001)
    0.28386...
    >>> annualize_return('0.1')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> annualize_return(-0.1)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(interest_rate, (int, float)) and interest_rate >= 0

    return (1 + interest_rate) ** DAYS_IN_YEAR - 1
