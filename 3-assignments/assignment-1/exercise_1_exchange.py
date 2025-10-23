# Students: you can remove this module if you don't use it.
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
    """

    # TODO: add defensive programming and corner cases here. Use
    # `string.ascii_uppercase` and `string.ascii_lowercase` to get all
    # letters allowed in currency codes.

    yahoo_code = f"{src.upper()}{dst.upper()}=X"
    exchange_rate = tools.get_yahoo_value(yahoo_code)

    return amount * exchange_rate
