'''

Given a binary matrix where 0 represents water and 1 represents land, and connected ones form an island, count the total islands.

Input:

[
	[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
	[0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
	[1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

Output: 5

Explanation: There are a total of 5 islands present in the above matrix. They are marked by the numbers 1 to 5 in the matrix below.

  1  0  2  0  0  0  3  3  3  3
  0  0  2  0  2  0  3  0  0  0
  2  2  2  2  0  0  3  0  0  0
  2  0  0  2  0  3  0  0  0  0
  2  2  2  2  0  0  0  5  5  5
  0  2  0  2  0  0  5  5  5  5
  0  0  0  0  0  5  5  5  0  0
  0  0  0  4  0  0  5  5  5  0
  4  0  4  0  4  0  0  5  0  0
  4  4  4  4  0  0  0  5  5  5

'''
from typing import List

def dfs(mat: List[List[int]], i: int, j: int):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] == 0:
        return
    
    # mark as visited
    mat[i][j] = 0
    dfs(mat, i - 1, j)  # Up
    dfs(mat, i + 1, j)  # Down
    dfs(mat, i, j - 1)  # Left
    dfs(mat, i, j + 1)  # Right
    dfs(mat, i + 1, j + 1) # Right Down Diagonal
    dfs(mat, i + 1, j - 1) # Right Up Diagonal
    dfs(mat, i - 1, j + 1) # Left Down Diagonal
    dfs(mat, i - 1, j - 1) # Left Up Diagonal

def count_islands(mat: List[List[int]]):
    islands = 0
    if len(mat) == 0:
        return islands
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                islands += 1
                dfs(mat, i, j)
    return islands

if __name__=="__main__":
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]
    ans = count_islands(mat=mat)
    print(ans)