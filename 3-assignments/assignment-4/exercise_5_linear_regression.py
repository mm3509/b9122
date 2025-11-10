import random


def helper_generate_data_miguel(duration):
    """
    >>> helper_generate_data_miguel(1)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming

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
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    # TODO: add a comment explaining why your data is a good counter-example to
    # the optimality of linear regression.

    return projects
