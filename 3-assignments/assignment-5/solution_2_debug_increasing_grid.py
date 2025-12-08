import random


def generate_increasing_grid(random_seed):
    """
    >>> grid = generate_increasing_grid(0)
    >>> isinstance(grid, list)
    True
    >>> len(grid) > 0
    True
    >>> len(grid[0]) > 0
    True
    >>> generate_increasing_grid("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(random_seed, int)

    random.seed(random_seed)

    horizontal = random.randrange(1, 50)
    vertical = random.randrange(1, 50)

    # Students: one bug was here. Using `* horizontal` used a view of the
    # original list, so we were always changing that one list.
    grid = [[0] * vertical for _ in range(horizontal)]

    for row in range(horizontal):
        for col in range(vertical):
            minima = []
            if 0 < row:
                minima.append(grid[row - 1][col])
            if 0 < col:
                minima.append(grid[row][col - 1])

            # Students: another bug was here: we should use max(), not min(),
            # in order to get a number that is larger than both the one in the
            # previous column and previous row.
            minimum = 0 if not minima else max(minima)

            number = 1 + minimum + random.randrange(100)

            grid[row][col] = number

            if 0 < row:
                assert number > grid[row - 1][col]
            if 0 < col:
                assert number > grid[row][col - 1]

    return grid
