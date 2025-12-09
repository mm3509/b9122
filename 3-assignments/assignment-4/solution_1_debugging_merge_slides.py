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

    # Students: this initializes the random number generator, so that your
    # answers are reproducible and match the ones from Autograder.
    random.seed(random_seed)

    original = random.randrange(1, 81)
    solutions = original + random.randrange(5)

    additional = []

    # Students: changing this to a while loop, and converting additional to a
    # unique list solves the bug. Alternatively, you could sample unique values
    # from the solution pages (and avoid the for/while loop entirely), with
    # this code:

    num_additional = solutions - original
    population = list(range(1, solutions + 1))
    additional = sorted(random.sample(population, num_additional))

    # while len(additional) != solutions - original:
    #     page = random.randrange(1, solutions + 1)
    #     additional.append(page)
    #     additional = sorted(set(additional))

    assert solutions == original + len(additional)

    return original, solutions, additional
