import statistics
import numpy as np


def check_expenses(expenses):
    assert isinstance(expenses, list)
    assert all([isinstance(element, (float, int)) for element in expenses])
    assert all([element >= 0 for element in expenses])


def check_duration(duration):
    assert isinstance(duration, int) and duration > 0


def check_budget(budget):
    assert isinstance(budget, (int, float)) and budget > 0


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
    >>> helper_normalize_budget([1, "2"], 20)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_normalize_budget([1, 2], 0)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_normalize_budget([1, -1], 20)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    check_expenses(expenses)
    check_budget(budget)

    factor = budget / sum(expenses)
    new_expenses = list([element * factor for element in expenses])
    assert np.isclose(sum(new_expenses), budget)

    return new_expenses


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
    >>> helper_shrink_or_stretch(123, 12)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_shrink_or_stretch(["1", 2], 12)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_shrink_or_stretch([1, 2], "1")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_shrink_or_stretch([1, 2], 0)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_shrink_or_stretch([-1, 2], 4)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    check_expenses(expenses)
    check_duration(duration)

    n_expenses = len(expenses)
    if duration < n_expenses:
        assert n_expenses % duration == 0
    else:
        assert duration % n_expenses == 0

    if n_expenses == duration:
        return expenses

    new_expenses = []
    if n_expenses < duration:
        stretch_factor = duration // n_expenses
        for i in range(n_expenses):
            for _ in range(stretch_factor):
                new_expenses.append(expenses[i] / stretch_factor)
    else:
        shrink_factor = n_expenses // duration
        for i in range(duration):
            start = i * shrink_factor
            end = start + shrink_factor
            new_expenses.append(sum(expenses[start:end]))

    # Students: this line confirms that the logic is correct and we don't miss
    # any part of the budget in the stretching or shrinking. In production
    # code, this is a good case for using an assertion error, which checks
    # internal consistency. For external consistency, like defensive
    # programming, production code uses ValueErrors or TypeErrors (but in this
    # course, we use assertions to save you time in typing).

    assert np.isclose(sum(new_expenses), sum(expenses))

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
    >>> predict_expenses(0, 10, [[1, 2, 3]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(1, "10", [[1, 2, 3]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(5, 0, [[1, 2, 3]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(1, 10, 123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(5, 10, [])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(5, 10, [123])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> predict_expenses(5, 10, [["1", 2]])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    check_budget(budget)
    check_duration(duration)

    assert isinstance(past_projects, list) and past_projects != []
    for expenses in past_projects:
        check_expenses(expenses)

    normalized_projects = []
    for project in past_projects:
        project_right_duration = helper_shrink_or_stretch(project, duration)

        project_normalized = helper_normalize_budget(project_right_duration,
                                                     budget)

        normalized_projects.append(project_normalized)

    cdtl_mean_list = []
    for i in range(duration):
        cdtl_mean = statistics.mean([project[i]
                                     for project in normalized_projects])
        cdtl_mean_list.append(cdtl_mean)

    return cdtl_mean_list
