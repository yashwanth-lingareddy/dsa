'''
Question:
Given an `N × N` integer matrix, rotate the matrix by 180 degrees in a clockwise direction. The transformation should be done in-place in quadratic time.

Input:

[
	[1,  2,  3,  4],
	[5,  6,  7,  8],
	[9,  10, 11, 12],
	[13, 14, 15, 16]
]

Output:

[
	[16, 15, 14, 13], 0
	[12, 11, 10, 9], 1
	[8,  7,  6,  5], 2
	[4,  3,  2,  1] 3
]

Solution:
1. Reverse each row of matrix
2. From the row-reveresed matrix reverse each column

l = 4
l - 

when j = 0, l = 4, i = 3
when j = 1, l = 4, i 

i,j = i,j
0,0 = 3,0
0,1 = 3,1
0,2 = 3,2
0,3 = 3,3

i,j = i,j
1,0 = 2,0
1,1 = 2,1
1,2 = 2,2
1,3 = 2,3
1,4 = 2,4


'''
from typing import List

def reverse_rows(matrix: List[List[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) // 2):
            matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

def reverse_columns(matrix: List[List[int]]):
    for i in range(len(matrix) // 2):
        for j in range(len(matrix[i])):
            matrix[i][j], matrix[len(matrix[i]) - i - 1][j] = matrix[len(matrix[i]) - i - 1][j], matrix[i][j]

def rotate_matrix(matrix: List[List[int]]):
    reverse_rows(matrix=matrix)
    reverse_columns(matrix=matrix)

if __name__=="__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(matrix=matrix)
    print(matrix)