'''

Given an `M × N` integer matrix, shift all its elements by `1` in spiral order.

Input:

[
	[ 1,  2,  3,  4, 5],
	[16, 17, 18, 19, 6],
	[15, 24, 25, 20, 7],
	[14, 23, 22, 21, 8],
	[13, 12, 11, 10, 9]
]

Output:

[
	[25,  1,  2,  3, 4],
	[15, 16, 17, 18, 5],
	[14, 23, 24, 19, 6],
	[13, 22, 21, 20, 7],
	[12, 11, 10,  9, 8]
]

'''

from typing import List

def shiftMatrix(mat: List[List[int]]) -> None:
    if len(mat) == 0:
        return
    if len(mat[0]) == 0:
        return

    m, n = len(mat), len(mat[0])

    # Create a list to store the spiral traversal
    spiral = []
    
    # Traverse the matrix in spiral order
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for col in range(left, right + 1):
            spiral.append(mat[top][col])
        top += 1
        
        # Traverse right column from top to bottom
        for row in range(top, bottom + 1):
            spiral.append(mat[row][right])
        right -= 1
        
        # Traverse bottom row from right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                spiral.append(mat[bottom][col])
            bottom -= 1
        
        # Traverse left column from bottom to top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                spiral.append(mat[row][left])
            left += 1
    
    # Shift the elements in the spiral list by 1
    shifted_spiral = spiral[-1:] + spiral[:-1]
    
    # Update the matrix with the shifted spiral
    top, bottom, left, right = 0, m - 1, 0, n - 1
    idx = 0
    while top <= bottom and left <= right:
        # Update top row from left to right
        for col in range(left, right + 1):
            mat[top][col] = shifted_spiral[idx]
            idx += 1
        top += 1
        
        # Update right column from top to bottom
        for row in range(top, bottom + 1):
            mat[row][right] = shifted_spiral[idx]
            idx += 1
        right -= 1
        
        # Update bottom row from right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                mat[bottom][col] = shifted_spiral[idx]
                idx += 1
            bottom -= 1
        
        # Update left column from bottom to top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                mat[row][left] = shifted_spiral[idx]
                idx += 1
            left += 1
    return

if __name__=="__main__":
    mat = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
    shiftMatrix(mat)
