def is_consistent(assignment, col, row):
    for c in assignment:
        r = assignment[c]
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True


def backtrack_csp(n, assignment=None):
    if assignment is None:
        assignment = {}

    if len(assignment) == n:
        return assignment

    col = len(assignment)
    for row in range(n):
        if is_consistent(assignment, col, row):
            assignment[col] = row
            result = backtrack_csp(n, assignment)
            if result:
                return result
            del assignment[col]

    return None


def solve_n_queens_csp(n):
    result = backtrack_csp(n)
    if result:
        return [result[i] for i in range(n)]
    else:
        return None
