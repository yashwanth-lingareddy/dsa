'''

Given an integer array whose elements may be misplaced by no more than `k` positions from the correct sorted order, efficiently sort it in linear time and constant space.

Input: nums[] = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
from typing import List

def sort_k_sorted_array(nums: List[int], k: int):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= max(0, i-k) and nums[j] > key:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key

if __name__=="__main__":
    nums =  [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    sort_k_sorted_array(nums, k)
    print(nums)
