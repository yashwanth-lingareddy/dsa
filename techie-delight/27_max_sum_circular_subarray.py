'''

Given a circular integer array, find a contiguous subarray with the largest sum in it.

Input : [2, 1, -5, 4, -3, 1, -3, 4, -1]
Output: 6
Explanation: Subarray with the largest sum is [4, -1, 2, 1] with sum 6.

Input : [8, -7, -3, 5, 6, -2, 3, -4, 2]
Output: 18
Explanation: Subarray with the largest sum is [5, 6, -2, 3, -4, 2, 8] with sum 18.

'''

from typing import List

def max_sub_array_sum(nums: List[int]) -> int:
    # Write your code here...
    if len(nums) < 1:
        return 0
        
    if len(nums) == 1:
        return nums[0]
    total_sum = nums[0]
    max_sum_until_this_numer = nums[0]
    max_sum_so_far = nums[0]
    min_sum_until_this_number = nums[0]
    min_sum_so_far = nums[0]
    
    for i in range(1, len(nums)):
        n = nums[i]
        total_sum += n
        max_sum_until_this_numer = max(n, max_sum_until_this_numer + n)
        max_sum_so_far = max(max_sum_until_this_numer, max_sum_so_far)
        min_sum_until_this_number = min(n, n + min_sum_until_this_number)
        min_sum_so_far = min(min_sum_until_this_number, min_sum_so_far)
    
    if max_sum_so_far > 0:
        # which means the max_sum_so_far is a positive number
        # wrapping the subarray can create a sum which is greater than max_sum_so_far
        return max(max_sum_so_far, total_sum - min_sum_so_far)
    else:
        # if the max sum is less than 0 then wrapping the subarray also will produce a sum less than 0
        # which will be lower than max_sum_so_far
        # return max_sum_so_far
        return max_sum_so_far

if __name__=="__main__":
    nums = [8, -7, -3, 5, 6, -2, 3, -4, 2]
    ans = max_sub_array_sum(nums)
    print(ans)