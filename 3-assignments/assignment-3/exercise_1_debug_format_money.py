MAX_LENGTH = 29


def helper_format_units(amount):
    """
    >>> helper_format_units(1000)
    '1,000'
    >>> helper_format_units(int(1e6))
    '1,000,000'
    """

    assert isinstance(amount, int)

    if amount < 1000:
        return str(amount)

    thousands = int(amount / 1000)
    units = amount - 1000 * thousands

    units_str = helper_format_units(units).zfill(3)

    return helper_format_units(thousands) + "," + units_str


def format_money(amount):
    """
    >>> format_money(-20.01)
    '                       -20.01'
    >>> format_money(1910.16)
    '                     1,910.16'
    >>> format_money(20)
    '                        20   '
    >>> format_money(-100)
    '                      -100   '
    >>> format_money(4000)
    '                     4,000   '
    >>> format_money(2625274418261258752)
    ' 2,625,274,418,261,258,752   '
    """

    assert isinstance(amount, (int, float))
    assert abs(amount) < int(1e20)

    if amount >= 0:
        sign = " "
    else:
        sign = "-"
        amount = abs(amount)

    amount_in_cents = round(amount * 100)
    amount_whole = int(amount_in_cents / 100)
    cents_only = amount_in_cents - 100 * amount_whole

    if 0 == cents_only:
        cent_str = " " * 3
    else:
        cent_str = "." + str(cents_only).zfill(2)

    amount_formatted = sign + helper_format_units(amount_whole) + cent_str

    return amount_formatted.rjust(MAX_LENGTH)
