def lower(astring):
    """
    >>> lower("ALLCAPS")
    'allcaps'
    >>> lower("all lowercase")
    'all lowercase'
    >>> lower("Title case")
    'title case'
    >>> lower("mIxEd CaSe")
    'mixed case'
    >>> lower("123ABC")
    '123abc'
    >>> lower("This is a sentence (with non-letter characters)")
    'this is a sentence (with non-letter characters)'
    >>> lower("These are French characters: Ç")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> lower(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>>
    """

    assert isinstance(astring, str)
    assert all([0 <= ord(c) <= 127 for c in astring])

    lowercase = []
    ordinal_A = ord("A")
    ordinal_Z = ord("Z")
    ordinal_a = ord("a")
    offset_to_lowercase = ordinal_a - ordinal_A

    for c in astring:
        ordinal_character = ord(c)
        if ordinal_A <= ordinal_character <= ordinal_Z:
            ordinal_character += offset_to_lowercase
        lowercase.append(chr(ordinal_character))

    return "".join(lowercase)
