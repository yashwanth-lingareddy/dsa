'''
Question:
Given an `N × N` integer matrix, rotate the matrix by 90 degrees in a clockwise direction. The transformation should be done in-place and in quadratic time.

Input:

[
	[1,  2,  3,  4],
	[5,  6,  7,  8],
	[9,  10, 11, 12],
	[13, 14, 15, 16],
]

Output:

[
	[13, 9,  5, 1],
	[14, 10, 6, 2],
	[15, 11, 7, 3],
	[16, 12, 8, 4]
]

Solution:
Steps to follow to rotate a matrix 90 degrees in a clockwise direction
1. Transpose the matrix - change rows to columns and columns to rows
2. Reverse the rows in matrix

Steps to follow to rotate a matrix 90 degrees in a anti-clockwise direction
1. Reverese the rows in matrix
2.  Transpose the matrix - change rows to columns and columns to rows

This question is 90 degrees clock wise
Transpose of Input:
[
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]

Reverese of Transposed Matrix:
[
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]
'''
from typing import List

def reverse_list(list: List[int]):
    for j in range(len(list) // 2):
        list[j] = list[len(list) - j + 1]

def reverse_matrix(matrix: List[List[int]]):
    for i in range(len(matrix)):
        # you can use built in reverse method or you can reverse yourself with custom logic
        # matrix[i].reverse()
        for j in range(len(matrix[i]) // 2):
            matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

def transpose_matrix(matrix: List[List[int]]):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotate_matrix(matrix: List[List[int]]):
    transpose_matrix(matrix)
    reverse_matrix(matrix)

if __name__=="__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(matrix=matrix)
    print(matrix)
