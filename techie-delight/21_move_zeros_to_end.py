'''

Given an integer array, in-place move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]


[6, 0, 8, 2, 3, 0, 4, 0, 1]
[6, 1, 8, 2, 3, 0, 4, 0, 0]

'''
from typing import List

def move_zeros_to_end(nums: List[int]):    
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1

if __name__=="__main__":
    nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    move_zeros_to_end(nums=nums)
    print(nums)