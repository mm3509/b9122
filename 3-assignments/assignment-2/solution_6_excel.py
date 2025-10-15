def number_to_excel_column(num):
    """
    >>> number_to_excel_column(1)
    'A'
    >>> number_to_excel_column(26)
    'Z'
    >>> number_to_excel_column(27)
    'AA'
    >>> number_to_excel_column(53)
    'BA'
    >>> number_to_excel_column("53")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> number_to_excel_column(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> number_to_excel_column(0)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(num, int) and 0 < num

    # Students: here is the recursive version:

    # if num <= 26:
    #     return chr(64 + num).upper()
    #
    # # Students: this divmod() function does the same thing as these two
    # # lines, but only in one line:
    #
    # # q = num // 26
    # # r = num % 26
    #
    # q, r = divmod(num, 26)
    # if r == 0:
    #     r = 26
    #     q -= 1
    #
    # return number_to_excel_column(q) + number_to_excel_column(r)

    # Students: here is the imperative version:

    column_letters_reversed = []
    while num > 0:

        # Students: see above for divmod(); the comment below is a good comment
        # that prevents deleting the `- 1` when you later revise the code.

        # Excel is 1-indexed, so subtract 1.
        num, remainder = divmod(num - 1, 26)
        letter = chr(ord("A") + remainder)

        # Students: Alternatively, use this (you'll need to import string):

        # letter = string.ascii_uppercase[remainder]

        column_letters_reversed.append(letter)

    return "".join(reversed(column_letters_reversed))


# Students: this part runs only if you run the file, not if you import it. It
# confirms that the results from this script coincide with those from OpenPyXL.
# You can run this part with this shell command: python solution_6_excel.py
if '__main__' == __name__:
    from openpyxl.utils.cell import get_column_letter

    for i in range(1, 3423):
        c = get_column_letter(i)
        assert c == number_to_excel_column(i)
    print("Your function coincides with OpenPyXL, well done!")
