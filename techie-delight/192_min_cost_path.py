'''

Given an `M × N` matrix of integers where each cell has a cost associated with it, find the minimum cost to reach the last cell (M-1, N-1) of the matrix from its first cell (0, 0). You can only move one unit right or one unit down from any cell, i.e., from cell (i, j), you can move to (i, j+1) or (i+1, j).

Input:

[
	[4, 7, 8, 6, 4],
	[6, 7, 3, 9, 2],
	[3, 8, 1, 2, 4],
	[7, 1, 7, 3, 7],
	[2, 9, 8, 9, 3]
]

Output: 36

Explanation: The highlighted path shows the minimum cost path having a cost of 36.

	4   7   8   6   4
	|
	6 — 7 — 3   9   2
			|
	3   8   1 — 2   4
				|
	7   1   7   3 — 7
					|
	2   9   8   9   3

'''

from typing import List

def min_cost_path(cost: List[List[int]]):
    if len(cost) == 0:
        return 0
    if (len(cost[0])) == 0:
        return 0
    m, n = len(cost), len(cost[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and first column
    dp[0][0] = cost[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    # Fill the remaining cells of dp
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])

    # Return the minimum cost to reach the last cell
    return dp[m-1][n-1]

if __name__=="__main__":
    cost = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
    ans = min_cost_path(cost=cost)
    print(ans)