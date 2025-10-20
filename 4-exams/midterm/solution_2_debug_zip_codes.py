import string


def is_valid_zip_code(zip_code):
    """
    >>> is_valid_zip_code('CB21HE')
    True
    >>> is_valid_zip_code('WC2H9JQ')
    True
    >>> is_valid_zip_code('10027')
    True
    >>> is_valid_zip_code(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> is_valid_zip_code('ABC')
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(zip_code, str)
    assert 4 <= len(zip_code)

    for char in zip_code:
        # The bug was in the next line. The boolean operator `or` on a
        # non-empty string like `string.digits` always evaluates to True. You
        # should use boolean operators like `and` and `or` only for
        # booleans. To test if a character is part of multiple strings, use
        # concatenation operator `+`.

        # Alternatively, you could fix it in this way, which is a bit longer:

        # if char not in string.ascii_letters and char not in string.digits:

        if char not in string.ascii_letters + string.digits:
            return False

    return True
