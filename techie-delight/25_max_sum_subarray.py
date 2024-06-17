'''

Given an integer array, find the maximum sum among all its subarrays.

Input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray is [4, -1, 2, 1]

Input : [-7, -3, -2, -4]
Output: -2
Explanation: The maximum sum subarray is [-2]

Input : [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
Output: 10
Explanation: The maximum sum subarray is [2, -1, 2, 1, 6] or [6, 4] or [2, -1, 2, 1, 6, -10, 6, 4]

'''

from typing import List

def max_sum_sub_array(nums: List[int]):
    if len(nums) < 1:
        return -1
    
    if len(nums) == 1:
        return nums[0]
    
    max_sum_until_this_number = nums[0]
    max_sum_so_far = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        max_sum_until_this_number = max(n, max_sum_until_this_number + n)
        max_sum_so_far = max(max_sum_so_far, max_sum_until_this_number)
    
    return max_sum_so_far


if __name__=="__main__":
    nums = [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
    ans = max_sum_sub_array(nums=nums)
    print(ans)