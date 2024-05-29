'''

Given an `M × N` integer matrix, return its elements in spiral order.

Input:

[
	[ 1   2   3   4  5],
	[16  17  18  19  6],
	[15  24  25  20  7],
	[14  23  22  21  8],
	[13  12  11  10  9]
]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
'''

from typing import List

def spiral_traversal(mat: List[List[int]]) -> List[int]:
    if len(mat) == 0:
        return []
    if len(mat[0]) == 0:
        return []
    
    m, n = len(mat), len(mat[0])

    # Create a list to store the spiral traversal
    spiral = []
    top_index, bottom_index = 0, m - 1 # row index
    left_index, right_index = 0, n - 1 # column index
    
    
    while top_index <= bottom_index and left_index <= right_index:
        # traversing from left to right 
        # top_index will be constant and left_index will go to right
        # that is increment left_index by 1 on each iteration, by keeping top_index constant
        for col in range(left_index, right_index + 1):
            spiral.append(mat[top_index][col])
        top_index += 1
        
        # traversing from top to bottom 
        # top_index will go down and right_index will be constant
        # that is increment top_index by 1 in each iteration, by keeping right_index constant
        for row in range(top_index, bottom_index + 1):
            spiral.append(mat[row][right_index])
        right_index -= 1
        
        # traversing from right to left
        # bottom_index will be constant and right_index will to left
        # that is decrement right_index by 1 in each iteration, by keeping bottom_index constant
        if top_index <= bottom_index:
            for col in range(right_index, left_index - 1, -1):
                spiral.append(mat[bottom_index][col])
            bottom_index -= 1
        
        # traversing from bottom to top
        # bottom_index will go up and left_index will be constant
        # that is decrement bottom_index by 1 in each, by keeping left_index constant
        if left_index <= right_index:
            for row in range(bottom_index, top_index - 1, -1):
                spiral.append(mat[row][left_index])
            left_index += 1
        
    return spiral

if __name__=="__main__":
    mat = [
        [1,2,3,4,5],
        [16,17,18,19,6],
        [15,24,25,20,7],
        [14,23,22,21,8],
        [13,12,11,10,9]
    ]
    ans = spiral_traversal(mat=mat)
    print(ans)