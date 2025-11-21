def repeat(txt, n):
    """
    >>> line1 = "this is a line"
    >>> line2 = "this is another line"
    >>> txt = "\\n".join([line1, line2])
    >>> new_txt = repeat(txt, 3)
    >>> new_lines = new_txt.split("\\n")
    >>> all([new_lines[i] == line1 for i in range(3)])
    True
    >>> all([new_lines[i] == line2 for i in range(3, 6)])
    True
    >>> repeat(123, 3)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return new_txt
