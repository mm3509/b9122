def helper_normalize_budget(expenses, budget):
    """
    >>> helper_normalize_budget([10, 20], 60)
    [20.0, 40.0]
    >>> helper_normalize_budget([40, 60], 20)
    [8.0, 12.0]
    >>> helper_normalize_budget(123, 20)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return


def helper_shrink_or_stretch(expenses, duration):
    """
    >>> helper_shrink_or_stretch([1, 2, 3], 6)
    [0.5, 0.5, 1.0, 1.0, 1.5, 1.5]
    >>> helper_shrink_or_stretch([1, 2, 3, 4, 5, 6], 3)
    [3, 7, 11]
    >>> helper_shrink_or_stretch([1, 2, 3], 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return new_expenses


def predict_expenses(budget, duration, past_projects):
    """
    >>> predict_expenses(100, 2, [[0, 50], [50, 0]])
    [50.0..., 50.0...]
    >>> predict_expenses(100, 2, [[0, 50], [50, 0], [50, 0]])
    [66.6..., 33.3...]
    >>> predict_expenses(100, 2, [[0, 50], [50, 0], [50, 50, 0, 0]])
    [66.6..., 33.3...]
    >>> predict_expenses("1", 10, [[1, 2, 3]])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return conditional_mean
