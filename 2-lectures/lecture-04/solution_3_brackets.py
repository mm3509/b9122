CORRESPONDENCE = {
    "}": "{",
    "]": "[",
    ")": "("
}
OPENERS = list(CORRESPONDENCE.values())
CLOSERS = list(CORRESPONDENCE.keys())


def is_valid(s):
    """
    >>> is_valid("{}[]{}()")
    True
    >>> is_valid("{}[}")
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
    >>> is_valid("[{]}")
    False
    >>> is_valid(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    """
    if not isinstance(s, str):
        raise ValueError("argument must be a string")
    
    if not s:
        return True

    for c in s:
        if c not in OPENERS + CLOSERS:
            return False

    stack = []
    for char in s:
        if char in OPENERS:
            stack.append(char)
            continue

        if not stack:
            return False
        
        last = stack.pop()
        if CORRESPONDENCE[char] != last:
            return False
        
    return 0 == len(stack)

