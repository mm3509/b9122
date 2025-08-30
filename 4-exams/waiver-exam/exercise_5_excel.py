import doctest

# Students: you may not import any other library.


def number_to_excel_column(num):
    """
    >>> number_to_excel_column(1)
    'A'
    >>> number_to_excel_column(26)
    'Z'
    >>> number_to_excel_column(27)
    'AA'
    >>> number_to_excel_column(52)
    'AZ'
    """

    # TODO: add defensive programming doc-tests for all possible
    # corner cases and complete this function to pass all doc-tests.
    return


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
