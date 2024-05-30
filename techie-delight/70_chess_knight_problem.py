'''

Given a chessboard, find the shortest distance (minimum number of steps) taken by a knight to reach a given destination from a given source.

Input:

N = 8 			(8 x 8 matrix)
src  = (0, 7)	(Source coordinates)
dest = (7, 0)	(Destination coordinates)

Output: 4

Explanation: The minimum number of steps required is 6. The knight's movement is illustrated in the following figure:

https://techiedelight.com/practice/images/Chess-Board.png


The solution should return -1 if the path is not possible.

'''

from collections import deque
from typing import Tuple

def is_safe(x, y, n):
    return 0 <= x < n and 0 <= y < n

def min_steps(src_x, src_y, dest_x, dest_y, n):
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    
    queue = deque([(src_x, src_y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[src_x][src_y] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == dest_x and y == dest_y:
            return distance
        
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if is_safe(new_x, new_y, n) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, distance + 1))
    
    return -1  # Destination not reachable

def find_shortest_distance(N: int, src: Tuple[int], dest: Tuple[int]) -> int:
    return min_steps(src[0], src[1], dest[0], dest[1], N)

if __name__=="__main__":
    N = 8
    src = tuple([0, 7])
    dest = tuple([7, 0])
    ans = find_shortest_distance(N, src, dest)
    print(ans)