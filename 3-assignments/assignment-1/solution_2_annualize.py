DAYS_IN_YEAR = 250


def annualize_return(interest_rate):
    """
    >>> round(annualize_return(0.001), 5)
    0.28387
    >>> annualize_return('0.1')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(interest_rate, (int, float))

    return (1 + interest_rate) ** DAYS_IN_YEAR - 1
