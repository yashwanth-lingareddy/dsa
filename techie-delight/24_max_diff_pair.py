'''

Given an integer array, find the maximum difference between two elements in it such that the smaller element appears before the larger element. If no such pair exists, return any negative number.

Input : [2, 7, 9, 5, 1, 3, 5]
Output: 7
Explanation: The pair with the maximum difference is (2, 9).

Input : [5, 4, 3, 2, 1]
Output: -1 (or any other negative number)
Explanation: No pair with the maximum difference exists.

'''
import sys

from typing import List

def max_difference_pair(nums: List[int]):
    if len(nums) < 2:
        return -1
    
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return -1
        return nums[1] - nums[0]
    
    max_difference = -1
    min_element = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        if n <= min_element:
            min_element = min(n, min_element)
        else:
            this_difference = n - min_element
            max_difference = max(this_difference, max_difference)
    
    return max_difference

if __name__=="__main__":
    nums = [1, 1, 1, 1]
    ans = max_difference_pair(nums=nums)
    print(ans)