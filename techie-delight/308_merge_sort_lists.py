'''

Given `M` sorted lists of variable length, merge them efficiently in sorted order.

Input:

mat = [
	[10, 20, 30, 40],
	[15, 25, 35],
	[27, 29, 37, 48, 93],
	[32, 33]
]

Output: [10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93]


Time Complexity = O(N log M) N = total number of elements across all lists, M = total number of lists
Space Complexity = O(M) for the heap, plus O(N) for the output list.

'''

import heapq
from typing import List

def merge_sorted_lists(lists: List[List[int]]) -> List[int]:
    # remove all empty lists
    lists = [l for l in lists if l]
    if not lists:
        return []
    
    ans = []
    heap = []

    # Add first element in each list along with the list index and element index to heap
    for i in range(len(lists)):
        element, list_index, element_index = lists[i][0], i, 0
        heapq.heappush(heap, (element, list_index, element_index))
    
    while len(heap) > 0:
        element, list_index, element_index = heapq.heappop(heap)
        ans.append(element)

        # if this list has next element, push the next element to the heap
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_element, list_index, element_index + 1))
    
    return ans

if __name__=="__main__":
    lists = [
        [10, 20, 30, 40],
        [15, 25, 35],
        [27, 29, 37, 48, 93],
        [32, 33]
    ]
    ans = merge_sorted_lists(lists=lists)
    print(ans) 