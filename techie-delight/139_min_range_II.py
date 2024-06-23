'''

Given M sorted lists of variable length, efficiently compute the smallest range, including at least one element from each list.

Input:

mat = [
	[3, 6, 8, 10, 15],
	[1, 5, 12],
	[4, 8, 15, 16],
	[2, 6],
]

Output: (4, 6)

Input:

mat = [
	[2, 3, 4, 8, 10, 15],
	[1, 5, 12],
	[7, 8, 15, 16],
	[3, 6],
]

Output: (4, 7)


If minimum range doesn't exist, the solution should return an empty tuple.

Input : [[], [], []]
Output: ()

'''
import heapq
from typing import List, Tuple

def find_min_range(lists: List[List[int]]) -> Tuple[int]:
    if not lists or any(not l for l in lists):
        return (-1, -1)
    
    heap = []
    max_element = float('-inf')
    
    # Initialize a heap with first value from each list, list index and element index
    for i in range(len(lists)):
        heapq.heappush(heap, (lists[i][0], i, 0))
        max_element = max(max_element, lists[i][0])
    
    min_range = float('inf')
    range_start, range_end = -1, -1
    while len(heap) > 0:
        min_element, lst_idx, min_element_index = heapq.heappop(heap)

        current_range = max_element - min_element
        if current_range < min_range:
            min_range = current_range
            range_start, range_end = min_element, max_element
        
        if min_element_index + 1 >= len(lists[lst_idx]):
            break

        next_value = lists[lst_idx][min_element_index + 1]
        heapq.heappush(heap, (next_value, lst_idx, min_element_index + 1))
        max_element = max(max_element, next_value)

    return (range_start, range_end)

if __name__=="__main__":
    lists = [
        [3, 6, 8, 10, 15],
        [1, 5, 12],
        [4, 8, 15, 16],
        [2, 6],
    ]
    ans = find_min_range(lists=lists)
    print(ans)