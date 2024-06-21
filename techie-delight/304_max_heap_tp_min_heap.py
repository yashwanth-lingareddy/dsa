'''

Given an array representing a max-heap, in-place convert it into the min-heap in linear time.

Input: [9, 4, 7, 1, -2, 6, 5]

		   9
		 /   \
		/	  \
	   4	   7
	  / \	  / \
	 /   \   /   \
	1	 -2 6	  5


Output: [-2, 1, 5, 9, 4, 6, 7]

		   -2
		 /	  \
		/	   \
	   1		5
	  / \	   / \
	 /   \	  /   \
	9	  4  6	   7		or, any other valid min-heap.

'''

from typing import List

def min_heapify(nums: List[int], i: int):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(nums) and nums[left] < nums[smallest]:
        smallest = left
    
    if right < len(nums) and nums[right] < nums[smallest]:
        smallest = right

    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        min_heapify(nums=nums, i=smallest)

def convert(nums: List[int]):
    for i in range(len(nums) // 2 - 1, -1, -1):
        min_heapify(nums, i)

if __name__=="__main__":
    nums = [9, 4, 7, 1, -2, 6, 5]
    convert(nums=nums)
    print(nums)