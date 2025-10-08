def generate_alphabet_backwards():
    """
    >>> generate_alphabet_backwards()
    'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    """

    start = ord("Z")  # Or 65 + 25
    end = ord("A") - 1  # Or 65 - 1
    
    # This is the solution with a for loop.
    alphabet_backwards = []
    for i in range(start, end, -1):
        alphabet_backwards.append(chr(i))

    # This is the solution with a list comprehension.
    alphabet_backwards = [chr(i) for i in range(start, end, -1)]
    return "".join(alphabet_backwards)

