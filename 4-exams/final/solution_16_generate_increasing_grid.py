def distribute_in_grid(numbers, horizontal, vertical):
    """
    >>> distribute_in_grid([1, 2, 3, 4], 2, 2)
    [[1, 3], [2, 4]]
    >>> distribute_in_grid(list(range(6)), 2, 3)
    [[0, 2, 4], [1, 3, 5]]
    >>> distribute_in_grid(list(range(6)), 3, 2)
    [[0, 2], [1, 4], [3, 5]]
    >>> distribute_in_grid(list(range(1, 10)), 3, 3)
    [[1, 3, 6], [2, 5, 8], [4, 7, 9]]
    >>> distribute_in_grid(list(range(5)), 1, 5)
    [[0, 1, 2, 3, 4]]
    >>> distribute_in_grid(list(range(4)), 4, 1)
    [[0], [1], [2], [3]]
    >>> distribute_in_grid([], 0, 0)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid(123, 2, 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([1, "2"], 1, 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([1, 2], "1", 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([1, 2], 0, 2)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([1, 2], 1, "2")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([1, 2], 1, 0)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> distribute_in_grid([2, 1], 2, 1)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(numbers, list) and 0 < len(numbers)
    assert all([isinstance(element, int) for element in numbers])
    assert sorted(numbers) == numbers

    for arg in [horizontal, vertical]:
        assert isinstance(arg, int) and 1 <= arg

    assert len(numbers) == horizontal * vertical

    grid = [[-1] * vertical for _ in range(horizontal)]

    diagonal = 0
    row = 0
    col = diagonal - row  # `row + col == diagonal` should always be true.

    for i in range(len(numbers)):
        grid[row][col] = numbers[i]
        row -= 1
        col += 1

        if row == -1 or vertical <= col:
            diagonal += 1
            row = diagonal
            col = 0

        if horizontal <= row:
            row = horizontal - 1
            col = diagonal - row

        if vertical <= col:
            col = 0
            row = diagonal - col

    return grid
