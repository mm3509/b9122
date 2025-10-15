import string


def excel_column_to_number(letters):
    """
    >>> excel_column_to_number("A")
    1
    >>> excel_column_to_number("b")
    2
    >>> excel_column_to_number("Z")
    26
    >>> excel_column_to_number("AA")
    27
    >>> excel_column_to_number("BA")
    53
    >>> excel_column_to_number(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> excel_column_to_number('')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> excel_column_to_number('ç')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(letters, str)

    assert "" != letters

    assert all([c in string.ascii_letters for c in letters])

    letters = letters.upper()

    # Students: here is the recursive version:

    # if 1 == len(letters):
    #     return ord(letters.upper()) - 64  # 65 is A
    #
    # last_letter = excel_column_to_number(letters[-1])
    # first_letters = excel_column_to_number(letters[:-1])
    #
    # return 26 * first_letters + last_letter

    # Students: here is the imperative version:

    column_number = 0
    for char in letters:

        # Excel columns are 1-based, so A = 1, not 0.
        value = ord(char) - ord("A") + 1

        # Students: Alternatively, you could use this:

        # value = string.ascii_uppercase.index(char) + 1

        column_number = column_number * 26 + value

    return column_number


# Students: this part runs only if you run the file, not if you import it. It
# confirms that the results from this script coincide with those from OpenPyXL.
# You can run this part with this shell command: python solution_5_excel.py
if '__main__' == __name__:
    from openpyxl.utils.cell import get_column_letter

    for i in range(1, 3423):
        c = get_column_letter(i)
        assert i == excel_column_to_number(c)
    print("Your function coincides with OpenPyXL, well done!")
