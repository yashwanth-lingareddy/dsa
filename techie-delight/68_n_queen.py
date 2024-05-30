'''

The N–queens puzzle is the problem of placing `N` chess queens on an `N × N` chessboard so that no two queens threaten each other. Thus, the solution requires that no two queens share the same row, column, or diagonal.

The solution should return a Set of the string representation of each possible solution to the N–Queens problem.

Input: N = 4
Output:
{
	'[[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]',
	'[[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]'
}

Here 1 represents the position of a queen in chessboard. Note that the solution exists for all natural numbers, except for 2 and 3. The solution should return an empty set for N = 2 and N = 3.

Input: N = 2
Output: {}

Note: To get the string representation of a solution to N–Queen's problem stored in List[List[int]], you can call built-in `str()` function.

'''
from typing import List, Set

def is_safe(board: List[List[int]], row: int, col: int, n: int):
    # Check the row
    if any(board[row][c] == 1 for c in range(col)):
        return False

    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board: List[List[int]], col: int, n: int, solutions: Set[int]):
    if col == n:
        solutions.add(str(board))
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, col + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens(n: int):
    solutions = set()
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0, n, solutions)
    return solutions

if __name__=="__main__":
    n = 4
    ans = solve_n_queens(n)
    print(ans)