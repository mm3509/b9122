import string


def clean_iban(iban):
    """
    >>> clean_iban("US123456789")
    'US123456789'
    >>> clean_iban("us12.3456 789")
    'US123456789'
    >>> clean_iban('us12. 34')
    'US1234'
    >>> clean_iban(1234)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> clean_iban('-US123456789')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> clean_iban('UÇ123456789')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> clean_iban('US123456789Z')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> clean_iban('US 12')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> clean_iban('U')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(iban, str)

    # Students: I do computations here because then the whole file is
    # more readable. If you try to run all defensive programming
    # first, the code will not be DRY and harder to read.
    clean_iban = iban.upper().replace(" ", "").replace(".", "")

    assert 4 < len(clean_iban)

    for c in clean_iban[:2]:
        assert c in string.ascii_letters

    for c in clean_iban[-2:]:
        assert c in string.digits

    for c in clean_iban[2:-2]:
        assert c in string.ascii_letters + string.digits

    return clean_iban


def are_same_iban(iban1, iban2):
    """
    >>> are_same_iban("US1234", "us12. 34")
    True
    >>> are_same_iban("US1234", "-us12. 34")
    Traceback (most recent call last):
    ...
    AssertionError
    """

    clean_iban1 = clean_iban(iban1)
    clean_iban2 = clean_iban(iban2)
    return clean_iban1 == clean_iban2
