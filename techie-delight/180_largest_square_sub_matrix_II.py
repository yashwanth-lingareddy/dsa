'''

Given an `M × N` binary matrix, find the size of the largest square submatrix of 1’s in it.

Input:

[
	[0, 0, 1, 0, 1, 1],
	[0, 1, 1, 1, 0, 0],
	[0, 0, 1, 1, 1, 1],
	[1, 1, 0, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 1],
	[1, 1, 1, 0, 1, 1]
]

Output: 3

Explanation: The largest square submatrix of 1’s is marked below by `x`.

	0  0  1  0  1  1
	0  1  1  1  0  0
	0  0  1  x  x  x
	1  1  0  x  x  x
	1  1  1  x  x  x
	1  1  0  1  0  1
	1  0  1  1  1  1
	1  1  1  0  1  1

    
Hint: Dynamic programming    
'''

from typing import List

def find_largest_square_sub_matrix(mat: List[List[int]]):
    if not mat:
        return 0

    m, n = len(mat), len(mat[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    # Initialize first row and first column
    for i in range(m):
        dp[i][0] = int(mat[i][0])
        max_side = max(max_side, dp[i][0])
    for j in range(n):
        dp[0][j] = int(mat[0][j])
        max_side = max(max_side, dp[0][j])

    # Fill the remaining cells of dp
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                max_side = max(max_side, dp[i][j])

    return max_side

if __name__=="__main__":
    mat = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    ans = find_largest_square_sub_matrix(mat)
    print(ans)