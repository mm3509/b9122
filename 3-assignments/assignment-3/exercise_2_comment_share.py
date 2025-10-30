def helper_percentage_to_int(s):
    """
    >>> helper_percentage_to_int("maximum share is 50%")
    50
    >>> helper_percentage_to_int("50%")
    50
    >>> helper_percentage_to_int("50.5%")
    50
    >>> helper_percentage_to_int("30% is the maximum comment share for...")
    30
    >>> helper_percentage_to_int(50)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return


def get_max_percentages(text):
    """
    >>> line1 = "Assignment 3"
    >>> line2 = "some details"
    >>> line3 = "Maximum comment share is 30%; for debugging, it's 90%."
    >>> line4 = "Maximum comment share is 40%"
    >>> get_max_percentages("\\n".join([line1, line2, line3]))
    {'default': 30, 'debug': 90}
    >>> get_max_percentages("\\n".join([line1, line2, line4]))
    {'default': 40, 'debug': 40}
    >>> get_max_percentages("Comment share is 30%\\nComment share is 40%")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    # Students: although \\n is a newline in doc-tests, in code a newline is
    # \n, with one escape character only. So this is how you can get the lines
    # in the text:
    lines = text.split("\n")

    return
