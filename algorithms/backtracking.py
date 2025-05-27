
def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens_util(board, col, solutions):
    n = len(board)
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens_util(board, col + 1, solutions)

def solve_n_queens_backtracking(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(board, 0, solutions)
    return solutions
