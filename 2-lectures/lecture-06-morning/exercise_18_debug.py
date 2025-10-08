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
    """

    assert isinstance(transactions, list)

    for tx in transactions:
        assert isinstance(tx, tuple)

    assert isinstance(keys_to_keep, list)

    for key in keys_to_keep:
        assert isinstance(key, str)

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
