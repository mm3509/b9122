import doctest


def allocate_transactions(transactions, keys_to_keep):
    """
    >>> tx1 = ("AAPL", "buy", 10)
    >>> tx2 = ("AAPL", "sell", 10)
    >>> tx3 = ("MSFT", "buy", 10)
    >>> transactions = [tx1, tx2, tx3]
    >>> allocated = allocate_transactions(transactions, ["AAPL", "MSFT"])
    >>> len(allocated["AAPL"]) == 2
    True
    >>> allocated["AAPL"][0] == tx1
    True
    >>> allocated["AAPL"][1] == tx2
    True
    >>> len(allocated["MSFT"]) == 1
    True
    >>> allocated["MSFT"][0] == tx3
    True
    >>> allocate_transactions('123', ['AAPL'])
    Traceback (most recent call last):
    ...
    TypeError: first argument ...
    >>> allocate_transactions(['1', '2'], 123)
    Traceback (most recent call last):
    ...
    TypeError: first argument ...
    >>> allocate_transactions(transactions, 123)
    Traceback (most recent call last):
    ...
    TypeError: second argument ...
    >>> allocate_transactions(transactions, [123, 456])
    Traceback (most recent call last):
    ...
    TypeError: second argument ...
    """

    if not isinstance(transactions, list):
        raise TypeError("first argument must be a list")

    for tx in transactions:
        if not isinstance(tx, tuple):
            raise TypeError("first argument must be a list of tuples")

    if not isinstance(keys_to_keep, list):
        raise TypeError("second argument must be a list")

    for key in keys_to_keep:
        if not isinstance(key, str):
            raise TypeError("second argument must be a list of strings")

    allocation = dict.fromkeys(keys_to_keep, [])

    for tx in transactions:
        key = tx[0]
        if key not in keys_to_keep:
            continue

        allocation[key].append(tx)

    return allocation


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
