def check_argument(prices):
    assert isinstance(prices, list)

    for p in prices:
        assert isinstance(p, (float, int))
        assert p >= 0


def maximize_profit(prices):
    """
    >>> maximize_profit([5, 6, 9, 2, 4, 5])
    4
    >>> maximize_profit([10, 5, 4, 3, 2, 0])
    0
    >>> maximize_profit('abc')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> maximize_profit([1, '0'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> maximize_profit([1, -1])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    check_argument(prices)
    max_profit = 0
    N = len(prices)
    for buying_day in range(N):
        for selling_day in range(buying_day + 1, N):
            profit = prices[selling_day] - prices[buying_day]
            if profit > max_profit:
                max_profit = profit

    return max_profit
