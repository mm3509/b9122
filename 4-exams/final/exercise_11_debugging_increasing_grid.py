import random


def generate_increasing_grid(seed):
    """
    >>> a = generate_increasing_grid(0)
    >>> all([a[0][i] > a[0][i - 1] for i in range(1, len(a[0]))])
    True
    >>> all([a[i][0] > a[i - 1][0] for i in range(1, len(a))])
    True
    >>> generate_increasing_grid("1")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(seed, int)

    random.seed(seed)

    horizontal = random.randrange(1, 50)
    vertical = random.randrange(1, 50)

    all_numbers = []

    grid = [[0] * vertical] * horizontal

    for row in range(horizontal):
        number = 0
        for col in range(vertical):
            minima = []
            if 0 < row:
                minima.append(grid[row - 1][col])
            if 0 < col:
                minima.append(grid[row][col - 1])

            minimum = 0 if not minima else min(minima)

            number = minimum + 1 + random.randrange(int(1e4))
            all_numbers.append(number)

            grid[row][col] = number

            if 0 < row:
                assert number > grid[row - 1][col]
            if 0 < col:
                assert number > grid[row][col - 1]

    return grid
