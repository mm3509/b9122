import string


import tools


def convert(amount, src, dst):
    """
    >>> euros = convert(1, src="USD", dst="EUR")
    >>> 0.8 < euros and euros < 0.9
    True
    >>> pounds = convert(1, src="usd", dst="gbp")
    >>> 0.7 < pounds and pounds < 0.8
    True
    >>> convert(-1, 'USD', 'EUR')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> convert('1', 'USD', 'EUR')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> convert(1, 123, 'EUR')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> convert(1, 'USD', 123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> convert(1, 'USDD', 'EUR')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> convert(1, 'USD', 'EURR')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(amount, (int, float))

    assert amount >= 0

    for currency in [src, dst]:
        assert isinstance(currency, str)

        assert 3 == len(currency)

        for c in currency:
            assert c in string.ascii_uppercase + string.ascii_lowercase

    yahoo_code = f"{src.upper()}{dst.upper()}=X"
    exchange_rate = tools.get_yahoo_value(yahoo_code)

    return amount * exchange_rate
