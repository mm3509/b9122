def solve_n_queens(n):
    solutions = []
    board = [-1] * n  # board[i] = column of queen in row i

    def is_valid(row, col):
        # Check previous rows
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            # Convert numeric board into printable layout
            solutions.append([
                "." * board[r] + "Q" + "." * (n - board[r] - 1)
                for r in range(n)
            ])
            return

        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


# Example usage:
if __name__ == "__main__":
    n = 8
    sols = solve_n_queens(n)
    print(f"Number of solutions for {n}-queens:", len(sols))
    for sol in sols[:3]:  # print a few example solutions
        for row in sol:
            print(row)
        print()
