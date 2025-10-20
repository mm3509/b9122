import string


def range_to_integer_list(range_str):
    """
    >>> range_to_integer_list("1-3,7")
    [1, 2, 3, 7]
    >>> range_to_integer_list("1,3-5,7")
    [1, 3, 4, 5, 7]
    >>> range_to_integer_list("")
    []
    >>> range_to_integer_list(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> range_to_integer_list("1-2?")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(range_str, str)
    for c in range_str:
        assert c in string.digits + "-,"

    if not range_str:  # Or: if "" == range_str:
        return []

    range_list = []
    for section in range_str.split(","):
        num_dashes = section.count("-")

        if 0 == num_dashes:
            range_list.append(int(section))
            continue

        # Students: you can "unpack" a list or tuple into multiple variables
        # like this:
        start, end = section.split("-")

        # Students: it does the same thing as this (as long as there are 2
        # values after the split):

        # numbers = section.split("-")
        # start = numbers[0]
        # end = numbers[1]

        for i in range(int(start), int(end) + 1):
            range_list.append(i)

        # Students: Alternatively, you could omit the for loop:

        # range_list.extend(list(range(int(start), int(end) + 1)))

    return range_list
