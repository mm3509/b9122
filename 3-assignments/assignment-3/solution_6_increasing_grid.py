# TODO: use this to introduce and motivate OOP: maintaining state, avoid
# passing arguments (and confusing them if they are in.


def get_rows_cols(grid):
    rows = len(grid)
    cols = len(grid[0])
    return rows, cols


def update_lower_bound_row(number_to_find, grid, lw_bd_row, up_bd_col):
    
    rows, cols = get_rows_cols(grid)
    new_lw_bd_row = -1

    for i in range(lw_bd_row + 1, rows):
        value = grid[i][up_bd_col - 1]
        if value < number_to_find:
            new_lw_bd_row = i
            continue

        if number_to_find < value:
            break

        return i, up_bd_col - 1

    if new_lw_bd_row == rows - 1:
        return None

    return new_lw_bd_row


def update_upper_bound_column(number_to_find, grid, lw_bd_row, up_bd_col):

    rows, cols = get_rows_cols(grid)
    new_up_bd_col = up_bd_col

    for column in range(up_bd_col - 1, -1, -1):
        value = grid[lw_bd_row + 1][column]

        if number_to_find < value:
            new_up_bd_col = column
            continue

        if value < number_to_find:
            break

        return lw_bd_row + 1, column

    if new_up_bd_col == 0:
        return None

    return new_up_bd_col


def find_number_in_grid(number, grid):
    """
    >>> find_number_in_grid(2, [[1, 2], [3, 4]])
    (0, 1)
    >>> find_number_in_grid(3, [[1, 2], [3, 4]])
    (1, 0)
    >>> None is find_number_in_grid(0, [[1, 2], [3, 4]])
    True
    >>> None is find_number_in_grid(5, [[1, 2], [3, 4]])
    True
    >>> find_number_in_grid("abc", [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_number_in_grid(1, 123)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(number, int)
    assert isinstance(grid, list)

    rows, cols = get_rows_cols(grid)

    if number < grid[0][0] or grid[rows - 1][cols - 1] < number:
        return None

    # Name for lower bound row; all numbers in this row or below are strictly
    # lower than the number to find.
    lw_bd_row = -1
    # Name for upper bound column; all numbers in this column or above are
    # strictly higher than the number to find.
    up_bd_col = cols
    while True:
        # Students: to pass multiple arguments without confusing them, you pass
        # them with the name of the argument, then an equal symbol, then the
        # variable holding that value (often, they are the same). This avoids
        # bugs in case they are in the wrong position (e.g., we pass row before
        # column, but the function definition expects column before row).
        lw_bd_row = update_lower_bound_row(number_to_find=number,
                                           grid=grid,
                                           lw_bd_row=lw_bd_row,
                                           up_bd_col=up_bd_col)

        if None is lw_bd_row:
            return None
        if isinstance(lw_bd_row, tuple):
            return lw_bd_row

        up_bd_col = update_upper_bound_column(number_to_find=number,
                                              grid=grid,
                                              lw_bd_row=lw_bd_row,
                                              up_bd_col=up_bd_col)

        if None is up_bd_col:
            return None
        if isinstance(up_bd_col, tuple):
            return up_bd_col
