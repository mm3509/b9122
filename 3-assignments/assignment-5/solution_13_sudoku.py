###############################################################################
#
# Solution with closures
#
###############################################################################

# Prompt:

# Consider the sudoku problem. Write a function that takes as input a list of
# lists, where each element in the inner list represents a call with a number
# from 1 to 9, or 0 if the cell is empty, and solves the sudoku with
# backtracking.


def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.
    board: 9x9 list of lists containing integers 1-9 or 0.
    Returns True if a solution exists, False otherwise.
    """

    def find_empty():
        """Return (row, col) of first empty cell, or None if full."""
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return r, c
        return None

    def is_valid(r, c, val):
        """Check if val can be placed at board[r][c]."""

        # Check row
        if any(board[r][x] == val for x in range(9)):
            return False

        # Check column
        if any(board[x][c] == val for x in range(9)):
            return False

        # Check 3×3 subgrid
        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == val:
                    return False

        return True

    def backtrack():
        """Recursive solver."""
        empty = find_empty()
        if not empty:
            return board  # solved

        r, c = empty

        for val in range(1, 10):
            if is_valid(r, c, val):
                board[r][c] = val

                if backtrack():
                    return board

                board[r][c] = 0  # undo

        return False

    return backtrack()


# Example usage:

# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# if solve_sudoku(board):
#     print("Solved:")
#     for row in board:
#         print(row)
# else:
#     print("No solution exists.")
