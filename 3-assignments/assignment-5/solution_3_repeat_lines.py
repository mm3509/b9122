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
    >>> repeat("123", "0")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> repeat("123", -1)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(txt, str)
    assert isinstance(n, int) and n >= 0

    new_lines = []
    lines = txt.split("\n")
    for line in lines:
        for _ in range(n):
            new_lines.append(line)

    return "\n".join(new_lines)
