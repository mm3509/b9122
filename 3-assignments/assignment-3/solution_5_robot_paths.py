def verify_grid(grid, value_type):

    assert isinstance(grid, list)
    assert 0 < len(grid)

    n = 0
    for row in grid:
        assert isinstance(row, list)
        if n == 0:
            n = len(row)
        assert n == len(row)
        assert all([isinstance(value, value_type) for value in row])

    assert 0 < n


def count_paths(grid):
    """
    >>> count_paths([[True, True], [True, True]])
    2
    >>> count_paths([[True] * 3] * 2)
    3
    >>> count_paths([[True] * 3] * 3)
    6
    >>> count_paths([[True, False], [True, True]])
    1
    >>> count_paths([[True]])
    1
    >>> count_paths([])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths([[]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths([[123]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths([[True, True], [False]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths([[True, True], [True, False]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> count_paths([[False, True], [True, True]])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    verify_grid(grid, bool)

    m = len(grid)
    n = len(grid[0])
    assert (m > 0 and n > 0)

    assert grid[0][0] and grid[m - 1][n - 1]

    num_paths_from_here = [[None] * n] * m

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                num_paths_from_here[i][j] = 1
                continue

            free = grid[i][j]
            if not free:
                num_paths_from_here[i][j] = 0
                continue

            if i == m - 1:
                num_paths_from_here[i][j] = num_paths_from_here[i][j + 1]
                continue

            if j == n - 1:
                num_paths_from_here[i][j] = num_paths_from_here[i + 1][j]
                continue

            num_paths_from_here[i][j] = (num_paths_from_here[i + 1][j] +
                                         num_paths_from_here[i][j + 1])

    return num_paths_from_here[0][0]
