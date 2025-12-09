import random


def generate_merge_slides(random_seed):
    """
    >>> a = generate_merge_slides(14)
    >>> original = a[0]
    >>> solutions = a[1]
    >>> additional = a[2]
    >>> solutions == original + len(additional)
    True
    >>> generate_merge_slides("abc")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(random_seed, int)

    # Students: this initializes the random number generator, so that the
    # answers are reproducible and the exercise raises a bug every time you run
    # it with the current code, instead of raising an error at random times.
    random.seed(random_seed)

    original = random.randrange(1, 81)
    solutions = original + random.randrange(5)

    additional = []
    for _ in range(solutions - original):
        page = random.randrange(1, solutions + 1)
        additional.append(page)

    additional = sorted(set(additional))

    # Students: this is the typical case of using assertions, to confirm the
    # internal validity of our code. If these assertions raise errors, it's our
    # fault and we need to change our code. If defensive programming checks
    # raise errors, it's the user's fault and they need to change their
    # arguments. Production code users `raise ValueError()` for defensive
    # programming and `assert` for internal checks; but to save you time, we
    # use `assert` for both in this course.

    assert solutions == original + len(additional)

    return original, solutions, additional
