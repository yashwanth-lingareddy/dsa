'''

Given a maze in the form of a binary rectangular matrix, find the length of the shortest path from a given source to a given destination. The path can only be constructed out of cells having value 1, and at any moment, you can only move one step in one of the four directions (Top, Left, Down, Right).

Input:

matrix = [
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src  = (0, 0)
dest = (5, 7)

Output: 12

Explanation: The shortest path from (0, 0) to (5, 7) has length 12. The shortest path is marked below with x.

[
	[x, x, x, x, x, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, x, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, x, x, x, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, x, x, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, x, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, x, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

Note: The solution should return -1 if no path is possible.

'''

from typing import List, Tuple
from collections import deque

def is_valid_co_ordinates(m: int, n: int, coordinates: Tuple[int]):
    x = coordinates[0]
    y = coordinates[1]

    return x >= 0 and x < m and y >= 0 and y < n

def find_shortest_path(mat: List[List[int]], src: Tuple[int], dest: Tuple[int]) -> int:
    m = len(mat)
    n = len(mat[0])
    if mat[src[0]][src[1]] == 0 or mat[dest[0]][dest[1]] == 0:
        return -1
  
    queue = deque([(src[0], src[1], 0)]) # initial row, column, distance

    while len(queue) > 0:
        row, column, distance = queue.popleft()

        if (row, column) == dest:
            return distance
        
        # Explore Neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir_row, dir_column in directions:
            new_row = row + dir_row
            new_column = column + dir_column

            if is_valid_co_ordinates(m, n, (new_row, new_column)) and mat[new_row][new_column] == 1:
                mat[new_row][new_column] = 0 # mark it as visited
                queue.append((new_row, new_column, distance + 1))

    return -1

if __name__ == "__main__":
   
    matrix = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
    src  = (0, 0)
    dest = (5, 7)
    ans = find_shortest_path(matrix, src, dest)
    print(ans)