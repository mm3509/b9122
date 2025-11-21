def generate_alphabet_backwards():
    """
    >>> generate_alphabet_backwards()
    'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    """

    # Solution with a list comprehension:
    
    # lst = [chr(i) for i in range(ord("Z"), ord("A") - 1, -1)]
    # return "".join(lst)

    # Solution with strings:

    # s = ""
    # for i in range(ord("Z"), ord("A") - 1, -1):
    #     s += chr(i)
    
    # Solution with lists and a for loop:
    
    lst = []
    
    for i in range(90, 64, -1):
        lst.append(chr(i))

    return lst

# This is how you can count the number of uppercase characters in a string with
# list comprehensions:

username = "MM3509@columbia.edu"

print(sum([65 <= ord(c) and ord(c) <= 90 for c in username]))
