import string


def string_to_cents(currency):
    """
    >>> string_to_cents("141")
    14100
    >>> string_to_cents("141.60")
    14160
    >>> string_to_cents('141.6')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_to_cents([])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_to_cents(' 141')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_to_cents('-141')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_to_cents('141..60')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(currency, str)

    for c in currency:
        assert c in string.digits + "."

    if "." in currency:
        assert 1 >= currency.count(".")
        assert currency[-3] == "."

    cents = round(100 * float(currency))

    # Sanity check: converting back to string should always return the
    # same thing. If not, we have a problem in the logic. This uses an
    # assertion, another feature of defensive programming, that I use
    # often but I don't ask it of you.
    
    if cents % 100 == 0 and "." not in currency:
        currency_2 = f"{cents // 100:d}"
    else:
        currency_2 = "%.2f" % (cents / 100)
    err_msg = ("Problem: mismatch in string conversion: "
               f"{currency_2} vs {currency}")
    assert currency_2 == currency, err_msg

    return cents
