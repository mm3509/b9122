import doctest
import string

# Students: you may not import any other library.


def excel_column_to_number(letters):
    """
    >>> excel_column_to_number("A")
    1
    >>> excel_column_to_number("b")
    2
    >>> excel_column_to_number("Z")
    26
    >>> excel_column_to_number("AA")
    27
    """

    # TODO: add defensive programming doc-tests for all possible
    # corner cases and complete this function to pass all doc-tests.
    # You can use `string.ascii_uppercase` to get all 26 uppercase
    # letters.
    return


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
