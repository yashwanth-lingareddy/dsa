'''

Given an `N × N` matrix, find the maximum sum submatrix present in it.

Input:

mat = [
	[-5, -6, 3, 1, 0],
	[9, 7, 8, 3, 7],
	[-6, -2, -1, 2, -4],
	[-7, 5, 5, 2, -6],
	[3, 2, 9, -5, 1]
]

Output:

[
	[7, 8, 3],
	[-2, -1, 2],
	[5, 5, 2],
	[2, 9, -5]
]

In case the multiple maximum sum submatrix exists, the solution can return any one of them.

'''
import sys
from typing import List

def find_matrix_sum(matrix: List[List[int]]):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

def find_all_submatrices(matrix: List[List[int]]):
    if len(matrix) == 0:
        return []
    m, n = len(matrix), len(matrix[0])
    submatrices = []

    # Iterate over all possible sizes of submatrices
    for size_i in range(1, m + 1):
        for size_j in range(1, n + 1):
            # Iterate over all possible starting positions for the current size
            for i in range(m - size_i + 1):
                for j in range(n - size_j + 1):
                    submatrix = []
                    # Extract the submatrix of the current size and starting position
                    for row in range(i, i + size_i):
                        submatrix.append(matrix[row][j:j+size_j])
                    submatrices.append(submatrix)

    return submatrices

def find_max_sum_sub_matrix(matrix: List[List[int]]):
    all_sub_matrix = find_all_submatrices(matrix=matrix)
    max_sum = -1 * sys.maxsize
    max_sum_sub_matrix = []
    for s in all_sub_matrix:
        this_sum = find_matrix_sum(s)
        if this_sum > max_sum:
            max_sum = this_sum
            max_sum_sub_matrix = s
    
    return max_sum_sub_matrix

if __name__=="__main__":
    mat = [
        [-5, -6, 3, 1, 0],
        [9, 7, 8, 3, 7],
        [-6, -2, -1, 2, -4],
        [-7, 5, 5, 2, -6],
        [3, 2, 9, -5, 1]
    ]
    ans = find_max_sum_sub_matrix(mat)
    print(ans)