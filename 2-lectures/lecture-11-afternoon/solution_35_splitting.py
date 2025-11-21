def split_heading(heading):
    """
    >>> split_heading("5 points for MSFE, 10 points for MSAFA")
    ['5 points for MSFE', '10 points for MSAFA']
    >>> split_heading("5 points for MSFE; 10 points for MSAFA")
    ['5 points for MSFE', '10 points for MSAFA']
    >>> split_heading("5 points for MSFE; 10 points for MSAFA, or something else")
    Traceback (most recent call last):
    ...
    AssertionError...
    """
    
    heading = heading.replace(",", ";")
    assert 1 == heading.count(";")

    return heading.split(";")

    # This is a long solution, which also works:

    fields = [heading]
    delimiters = [", ", "; ", "/ ", "| ",]
    for delimiter in delimiters:
        new_fields = []
        for field in fields:
            new_fields.extend(field.split(delimiter))
        fields = new_fields

    assert 2 == len(new_fields)
    return new_fields
