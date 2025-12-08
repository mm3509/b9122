###############################################################################
#
# Solution without closures
#
###############################################################################

# Prompt:

# Forget everything I have told you so far. Consider the sudoku problem. Write
# a script without object-oriented programming, and without closures, that
# takes as input a list of lists, where each element in the inner list
# represents a call with a number from 1 to 9, or None if the cell is empty;
# that solves the sudoku with backtracking; and returns True if the sudoku has
# a solution and False if it hasn't.

def find_empty(board):
    """Return (row, col) of the first empty cell (None), or None if full."""
    for r in range(9):
        for c in range(9):
            if board[r][c] is None:
                return r, c
    return None


def is_valid(board, row, col, val):
    """Check whether val can be placed at (row, col)."""

    # Check row
    for c in range(9):
        if board[row][c] == val:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == val:
            return False

    # Check 3×3 subgrid
    start_r = (row // 3) * 3
    start_c = (col // 3) * 3

    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            if board[r][c] == val:
                return False

    return True


def backtrack(board):
    """Recursive solver."""
    empty = find_empty(board)
    if empty is None:
        return board  # Solved

    row, col = empty

    for val in range(1, 10):
        if is_valid(board, row, col, val):
            board[row][col] = val

            if backtrack(board):
                return board

            board[row][col] = None  # Undo

    return False


def solve_sudoku(board):
    """
    Solves the Sudoku puzzle.
    board is modified in place.
    Returns True if solvable, False if not.
    """
    return backtrack(board)

# Example usage: same as the previous exercise.
