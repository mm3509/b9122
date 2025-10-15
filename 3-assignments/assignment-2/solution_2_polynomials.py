def assert_list_of_numbers(A):
    assert isinstance(A, list)

    for a in A:
        assert isinstance(a, (int, float))

    # Alternatively, with a list comprehension:

    # assert all([isinstance(a, (int, float)) for a in A])


def evaluate_polynomial(x, A):
    """
    >>> a = evaluate_polynomial(1, [1, 2, 3])
    >>> round(a)
    6
    >>> evaluate_polynomial(1, [])
    0
    >>> evaluate_polynomial('0', [1])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> evaluate_polynomial(1, 123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> evaluate_polynomial(1, [1, '2', 3])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(x, (int, float))

    assert_list_of_numbers(A)

    value = 0

    # Students: enumerate() is a convenient way to iterate over both the index
    # and the element of a list.
    for power, coefficient in enumerate(A):
        value += coefficient * x ** power

    # Alternatively:

    # for power in range(len(A)):
    #     value += A[power] * x ** power

    return value


def evaluate_polynomial_fast(x, A):
    """
    >>> round(evaluate_polynomial_fast(1, [1, 2, 3]))
    6
    >>> evaluate_polynomial_fast(1, [])
    0
    >>> evaluate_polynomial_fast('0', [1])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> evaluate_polynomial_fast(1, 123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> evaluate_polynomial_fast(1, [1, '2', 3])
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # Students: if you already programmed the fast version in the function
    # above, do NOT copy-paste the code. Instead, use this:

    # return evaluate_polynomial(x, A)

    assert isinstance(x, (int, float))

    assert_list_of_numbers(A)

    accumulator = 0

    # Students: reversed() returns a new list in reverse order.
    for coefficient in reversed(A):
        accumulator = accumulator * x + coefficient

    # Alternatively:

    # for i in range(len(A) - 1, -1, -1):
    #     accumulator = accumulator * x + A[i]

    return accumulator
