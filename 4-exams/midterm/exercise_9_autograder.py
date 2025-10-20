import numpy as np


BOOL_TYPES = (bool, np.bool_)
NUMBER_TYPES = (int, float, np.float64)
ALL_TYPES = [BOOL_TYPES, NUMBER_TYPES, list, dict, str]


def helper_are_floats_equal(correct, student):
    """
    >>> helper_are_floats_equal(49, 48.999999)
    True
    """

    # Students: you don't need to do anything here.

    # Students: it's important to use bool(), which casts np.True_ to
    # True. Otherwise, the doc-tests fail on Autograder, where they show
    # `np.True_` instead of `True`.
    return bool(np.isclose(correct, student))


def are_answers_equal(correct, student):
    """
    >>> are_answers_equal(49, 48.9999999)
    True
    >>> are_answers_equal([1, 2, 3], [1, 2, 3])
    True
    >>> are_answers_equal([1, 2.00000001], [1, 2])
    True
    >>> are_answers_equal({"a": [1, 2.00000001]}, {"a": [1, 2]})
    True
    >>> are_answers_equal({"x": 1.00000001}, {"x": 1})
    True
    >>> are_answers_equal("abc", "abc")
    True
    >>> are_answers_equal("abc", "abd")
    False
    >>> are_answers_equal([None, None, 49], [None, 48, 48.9999999999])
    False
    >>> dict1 = {"MSFT": ["NYSE", 50000, 0.1]}
    >>> dict2 = {"MSFT": ["NYSE", 50000, 0.099999]}
    >>> are_answers_equal(dict1, dict2)
    True
    >>> dict1 = {"MSFT": 1, "AAPL": 2}
    >>> dict2 = {"AAPL": 2, "MSFT": 1}
    >>> are_answers_equal(dict1, dict2)
    True
    >>> dict1 = {"MSFT": 1, "AAPL": 2}
    >>> dict2 = {"AAPL": 2}
    >>> are_answers_equal(dict1, dict2)
    False
    >>> are_answers_equal(True, np.True_)
    True
    >>> are_answers_equal(True, np.False_)
    False
    >>> are_answers_equal((1, 2), [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    # Students: it's important to use bool(), which casts np.True_ to
    # True. Otherwise, the doc-tests fail on Autograder, where they show
    # `np.True_` instead of `True`.
    return bool(correct == student)
