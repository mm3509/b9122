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
        if char not in string.ascii_letters or string.digits:
            return False

    return True
