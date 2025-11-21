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

    grid = [[0] * vertical] * horizontal

    for row in range(horizontal):
        for col in range(vertical):
            minima = []
            if 0 < row:
                minima.append(grid[row - 1][col])
            if 0 < col:
                minima.append(grid[row][col - 1])

            minimum = 0 if not minima else min(minima)

            number = minimum + 1 + random.randrange(100)

            grid[row][col] = number

            if row > 0:
                assert number > grid[row - 1][col]
            if col > 0:
                assert number > grid[row][col - 1]

    return grid
