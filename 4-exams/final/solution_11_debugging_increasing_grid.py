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

    # Students: one bug was here: this expression creates multiple views of the
    # `[0] * vertical` list, so any change to one of them affects them all.**

    # grid = [[0] * vertical] * horizontal

    # Use a list comprehension to avoid multiple views on the same inner list.
    grid = [[0] * vertical for _ in range(horizontal)]

    for row in range(horizontal):
        number = 0
        for col in range(vertical):
            minima = []
            if 0 < row:
                minima.append(grid[row - 1][col])
            if 0 < col:
                minima.append(grid[row][col - 1])

            # Students: another bug was here: using min(minima) means it was
            # increasing only in one direction.

            # Use max(), not min(), so the number increases in both directions.
            minimum = 0 if not minima else max(minima)

            number = minimum + 1 + random.randrange(int(1e4))
            all_numbers.append(number)

            grid[row][col] = number

            if 0 < row:
                assert number > grid[row - 1][col]
            if 0 < col:
                assert number > grid[row][col - 1]

    return grid
