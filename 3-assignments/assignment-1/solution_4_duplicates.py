def remove_immediate_duplicate_lines(a_list):
    """
    >>> remove_immediate_duplicate_lines(['a', 'b', 'b', 'c'])
    ['a', 'b', 'c']
    >>> remove_immediate_duplicate_lines(['a', 'b', 'c', 'b'])
    ['a', 'b', 'c', 'b']
    >>> remove_immediate_duplicate_lines('abc')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> remove_immediate_duplicate_lines(['a', 123])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(a_list, list)

    for element in a_list:
        assert isinstance(element, str)

    last_element = None
    clean_list = []
    for element in a_list:
        if element != last_element:
            clean_list.append(element)
            last_element = element

    return clean_list


def print_non_duplicate_lines(fp):
    """
    This function serves for you, students, in case you need to
    remove duplicate lines from a file.  You do not need to complete
    it and it will not be graded.
    """

    with open(fp, encoding='utf-8') as f:
        contents = f.read()
    lines = contents.split('\n')
    clean = remove_immediate_duplicate_lines(lines)
    print("\n".join(clean))
