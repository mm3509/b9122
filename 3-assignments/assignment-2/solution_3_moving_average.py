import solution_2_polynomials


def check_arguments(A, n):
    solution_2_polynomials.assert_list_of_numbers(A)
    assert 0 < len(A)

    assert isinstance(n, int)
    assert n > 0
    assert n <= len(A)


def moving_average(A, n):
    """
    >>> a = moving_average([1, 3, 5, 11], 2)
    >>> a[0] is None
    True
    >>> round(a[1])
    2
    >>> round(a[2])
    4
    >>> round(a[3])
    8
    >>> moving_average([], 1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average('123', 2)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average([1, None, 3], 2)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average([2, 3], '1')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average([2, 3], 0)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average([2, 3], 3)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    check_arguments(A, n)

    # Students: add _list suffix to avoid confusion with the function name.
    moving_average_list = []

    # Students: you can start a list of size (n - 1) filled with None's like
    # this:
    start = [None] * (n - 1)

    # Alternatively: [None for _ in range(n - 1)]
    start = []
    for _ in range(n - 1):
        start.append(None)

    for i in range(n, len(A) + 1):
        total = 0
        for j in range(i - n, i):
            total += A[j]

        moving_average_list.append(total / n)

    return start + moving_average_list


def moving_average_fast(A, n):
    """
    >>> a = moving_average_fast([1, 3, 5, 11], 2)
    >>> a[0] is None
    True
    >>> round(a[1])
    2
    >>> round(a[2])
    4
    >>> round(a[3])
    8
    >>> moving_average_fast([], 1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average_fast('123', 2)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average_fast([1, None, 3], 2)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average_fast([2, 3], '1')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average_fast([2, 3], 0)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> moving_average_fast([2, 3], 3)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # Students: if you already programmed the fast version in the function
    # above, do NOT copy-paste the code. Instead, use this:

    # return moving_average(A, n)

    check_arguments(A, n)

    start = [None] * (n - 1)

    current_sum = 0

    # AFA students: A[:n] is "slice" notation and returns a list up to but excluding n.
    for value in A[:n]:
        current_sum += value

    # Alternatively, without slice notation:
    # for i in range(n):
    #     current_sum += A[i]

    moving_average_list = [current_sum / n]

    for i in range(n, len(A)):
        current_sum += A[i] - A[i - n]
        moving_average_list.append(current_sum / n)

        # Students: Alternatively, you could avoid keeping track of the current
        # sum, like this:

        # new_moving_average = moving_average_list[-1] + (A[i] - A[i - n]) / n
        # moving_average_list.append(new_moving_average)

    return start + moving_average_list
