CORRESPONDENCE = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}

OPENING_BRACKETS = CORRESPONDENCE.keys()
CLOSING_BRACKETS = CORRESPONDENCE.values()

def is_valid(s):
    """
    >>> is_valid("{}[]{}()")
    True
    >>> is_valid("{}[}")
    False
    >>> is_valid("{[}]")
    False
    >>> is_valid("{{{[()]}}}")
    True
    >>> is_valid("}")
    False
    >>> is_valid("{{}")
    False
    >>> is_valid("{a}")
    False
    >>> is_valid("")
    True
    >>> is_valid(123)
    Traceback (most recent call last):
    ...
    ValueError: ...
    """

    if not isinstance(s, str):
        raise ValueError("...")

    stack = []

    for char in s:
        if char not in list(OPENING_BRACKETS) + list(CLOSING_BRACKETS):
            return False

        if char in OPENING_BRACKETS:
            stack.append(char)
            continue
        
        if stack == []:
            return False
        
        last = stack.pop()
        if char != CORRESPONDENCE[last]:
            return False

    return stack == []
