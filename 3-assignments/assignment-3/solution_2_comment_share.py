DELIMITER = ";"


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
    >>> helper_percentage_to_int("50")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_percentage_to_int(" %")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_percentage_to_int(" 50.nonsense%")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(s, str)
    assert 1 == s.count("%")

    percentage = s.index("%")
    space = s[:percentage].rfind(" ")
    number = s[space + 1: percentage]
    try:
        return int(float(number))
    except ValueError:
        assert False


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
    >>> get_max_percentages("comment share: 30%, debug comment share: 40%")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> get_max_percentages("Assignment 3 details\\nFor this assignment..")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> get_max_percentages("Maximum comment share is 40")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> get_max_percentages("Debug comment share 40%; debug comment share 30%")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> get_max_percentages("comment share 40%; comment share 30%")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(text, str)

    # Students: alternatively, you could find matching lines with a list
    # comprehension and a conditional, like this:

    # matching_lines = [line for line in text.split("\n")
    #                   if "comment share" in line.lower()]

    lines = text.split("\n")
    matching_lines = []
    for line in lines:
        if "comment share" in line.lower():
            matching_lines.append(line)
            percentage_count = line.count("%")
            assert 1 <= percentage_count <= 2
            if 2 == percentage_count:
                assert 1 == line.count(";")
                assert "debug" in line

    assert 1 == len(matching_lines)
    matching_line = matching_lines[0]

    parts = matching_line.split(DELIMITER)
    assert 2 >= len(parts)

    if 1 == len(parts):
        percent = helper_percentage_to_int(matching_line)
        return {"default": percent, "debug": percent}

    debug = None
    default = None
    for piece in parts:
        if "debug" in piece.lower():
            debug = piece
        else:
            default = piece

    assert None is not default and None is not debug

    return {"default": helper_percentage_to_int(default),
            "debug": helper_percentage_to_int(debug)}
