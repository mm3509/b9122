TOTAL_LENGTH = 7


def format_money(amount):
    """
    >>> format_money(20)
    '  20   '
    >>> format_money(-20.01)
    ' -20.01'
    >>> format_money(910.16)
    ' 910.16'
    >>> format_money(910.1)
    ' 910.10'
    >>> format_money(-100)
    '-100   '
    >>> format_money(0)
    '   0   '
    >>> format_money("123")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> format_money(1000)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> format_money(-1000)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(amount, (int, float))
    assert abs(amount) < 1000

    negative = amount < 0
    amount = abs(amount)

    units_cents_integer = round(amount * 100)
    units, cents = divmod(units_cents_integer, 100)

    amount_str = str(units)

    if negative:
        amount_str = "-" + amount_str

    if 0 == cents:
        # Students: you can multiply a string N times with this syntax:
        amount_str += " " * 3  # Or: += "   "
    else:
        amount_str += "."
        if cents < 10:
            amount_str += "0"
        amount_str += str(cents)

    padding = TOTAL_LENGTH - len(amount_str)

    return " " * padding + amount_str
