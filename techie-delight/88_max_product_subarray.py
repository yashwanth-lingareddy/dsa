'''

Given an integer array, find the contiguous subarray that has the maximum product of its elements. The solution should return the maximum product of elements among all possible subarrays.

Input : [-6, 4, -5, 8, -10, 0, 8]
Output: 1600
Explanation: The maximum product subarray is [4, -5, 8, -10] which has product 1600.

Input : [40, 0, -20, -10]
Output: 200
Explanation: The maximum product subarray is [-20, -10] which has product 200.

Input : [10]
Output: 10

Input : []
Output: 0

'''

from typing import List

def find_max_product(nums: List[int]) -> int:
    # Write your code here...
    if len(nums) == 0:
        return 0
    if len(nums) == 0:
        return 0
    max_so_far = nums[0]
    min_ending_here = max_ending_here = nums[0]

    for i in range(1, len(nums)):
        temp = max_ending_here
        max_ending_here = max(nums[i], max(nums[i] * max_ending_here, nums[i] * min_ending_here))
        min_ending_here = min(nums[i], min(nums[i] * temp, nums[i] * min_ending_here))
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

if __name__=="__main__":
    nums = [-6, 4, -5, 8, -10, 0, 8]
    ans = find_max_product(nums=nums)
    print(ans)

