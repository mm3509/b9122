import string


def clean_iban(iban):
    """
    >>> clean_iban("US123456789")
    'US123456789'
    >>> clean_iban("us12.3456 789")
    'US123456789'
    """

    # TODO: add defensive programming.

    # TODO: add code to pass the doc-tests.

    clean_iban = ""

    return clean_iban


def are_same_iban(iban1, iban2):
    """
    >>> are_same_iban("US1234", "us12. 34")
    True
    """

    # TODO: add code. (No need for doc-tests, since errors are handled
    # by `clean_iban()`.)

    same = False
    return same
