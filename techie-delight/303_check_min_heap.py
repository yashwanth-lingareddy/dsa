'''
Given an integer array, check if it represents min-heap or not.

Input : [2, 3, 4, 5, 10, 15]
Output: True
Explanation: The input represents a min-heap.

		   2
		 /   \
		/	  \
	   3	   4
	  / \	  /
	 /   \   /
	5	 10 15

Input : [2, 10, 4, 5, 3, 15]
Output: False
Explanation: The input is not a min-heap, as it violate the heap property.

		   2
		 /   \
		/	  \
	   10	   4
	  / \	  /
	 /   \   /
	5	  3 15

    
Hint: A min-heap is a tree data structure where root node is greater than it's left and right nodes.
Programatically min heap is represented as list where element at `i` is root ndoe, element at `2 * i + 1` is left node and element at `2 * i + 2` is right node
so we have check for every node, if the element at that node is less than left and right if exists
'''
from typing import List

def is_min_heap(nums: List[int]):
    for i in range(len(nums)):
        left = 2 * i + 1
        right = left + 1
        if left < len(nums) and nums[left] < nums[i]:
            return False
        if right < len(nums) and nums[right] < nums[i]:
            return False
            
    return True

if __name__=="__main__":
    nums = [2, 3, 4, 5, 10, 15]
    ans = is_min_heap(nums)
    print(ans)
