def profitability(buying_price, selling_price):
    """
    >>> a = profitability(2, 4)
    >>> round(a)
    100
    >>> b = profitability(4, 2)
    >>> round(b)
    -50
    >>> c = profitability(1, 0)
    >>> round(c)
    -100
    >>> profitability(1, -1)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> profitability("1", 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> profitability(2, [])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    for p in [buying_price, selling_price]:
        assert isinstance(p, (int, float))
    assert buying_price > 0
    assert selling_price >= 0

    growth = (selling_price - buying_price) / buying_price

    # Alternative:
    # growth = selling_price / buying_price - 1

    return 100 * growth
