import random


def helper_generate_data_miguel(duration):
    """
    >>> helper_generate_data_miguel(1)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> helper_generate_data_miguel("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(duration, int) and duration > 1

    # Students: to generate a random integer between 50 and 100 (but
    # excluding 100), use this code: random.randrange(50, 100) .

    # Students: this generates an inverted V-shape of expenses per month.

    projects = []
    for i in range(10):
        project = []
        for month in range(duration):
            if month <= duration // 2:
                project.append(10 * month + random.randrange(10))
            else:
                project.append(10 * (duration - month) + random.randrange(10))

        projects.append(project)

    return projects


def generate_data_student(duration):
    """
    >>> generate_data_student(1)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> generate_data_student("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(duration, int) and duration > 1

    # If all past projects had around half of previous expenses in the first
    # month and half in the last month, the new project should also have all
    # expenses in either the first or last month, but linear regression
    # predicts constant expenses.

    # Another possible pattern is that all expenses come at the beginning
    # (resp. ending), and so the new project should behave the same way, but
    # linear regression predicts a linear decreasing pattern
    # (resp. increasing).

    # Another possible pattern is a jump in expenses, which are clustered near
    # $1000 for the first half, and around $2000 for the second half.

    # Yet another possible pattern is an exponential increase in expenses, and
    # linear regression predicts negative expenses at the start.

    projects = []
    for i in range(10):
        start = random.randrange(50, 100)
        end = random.randrange(50, 100)
        projects.append([start] + [0] * (duration - 2) + [end])

    return projects
