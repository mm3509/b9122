class SudokuSolver:
    def __init__(self, board):
        """
        board: 9x9 list of lists containing integers 1–9 or None.
        """
        self.board = board

    def solve(self):
        """Public method to solve the Sudoku."""
        return self._backtrack()

    def _find_empty(self):
        """Find the next empty cell (None). Returns (row, col) or None."""
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None

    def _is_valid(self, r, c, val):
        """Check whether val can be placed at (r, c)."""

        # Row check
        if any(self.board[r][i] == val for i in range(9)):
            return False

        # Column check
        if any(self.board[i][c] == val for i in range(9)):
            return False

        # 3×3 box check
        box_r = (r // 3) * 3
        box_c = (c // 3) * 3

        for i in range(box_r, box_r + 3):
            for j in range(box_c, box_c + 3):
                if self.board[i][j] == val:
                    return False

        return True

    def _backtrack(self):
        """Recursive backtracking solver."""
        empty = self._find_empty()
        if not empty:
            return self.board  # Solved

        r, c = empty

        for val in range(1, 10):
            if self._is_valid(r, c, val):
                self.board[r][c] = val

                if self._backtrack():
                    return self.board

                # Undo move
                self.board[r][c] = 0

        return False


# Example usage:

if "__main__" == __name__:
    board = [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9]
    ]

    solver = SudokuSolver(board)

    if solver.solve():
        print("Sudoku solved:")
        for row in board:
            print(row)
    else:
        print("No solution exists.")
