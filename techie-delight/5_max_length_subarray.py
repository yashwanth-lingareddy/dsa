'''
Question:
Given an integer array, find the maximum length contiguous subarray having a given sum.

Input : nums[] = [5, 6, -5, 5, 3, 5, 3, -2, 0], target = 8
Output: [-5, 5, 3, 5]
Explanation: The subarrays with sum 8 are [[-5, 5, 3, 5], [3, 5], [5, 3]]. The longest subarray is [-5, 5, 3, 5] having length 4.

Note: Since an input can contain several maximum length subarrays with given sum, the solution should return any one of the maximum length subarray.

'''
from typing import List

def max_length_subarray(nums: List[int], target: int) -> List[int]:
    prefix_sum = 0
    prefix_index = {0: [-1]}
    max_length_subarray = []
    for i in range(len(nums)):
        this_number = nums[i]
        prefix_sum += this_number
        this_sub_array = []
        if prefix_sum == target:
            this_sub_array = nums[0:i+1]
        
        complement = prefix_sum - target

        if complement in prefix_index:
            start_index = prefix_index[complement][0] + 1
            this_sub_array = nums[start_index:i+1]
        
        prefix_index[prefix_sum] = prefix_index.get(prefix_sum, []) + [i]
        if len(this_sub_array) > len(max_length_subarray):
            max_length_subarray = this_sub_array
    
    return max_length_subarray


if __name__=="__main__":
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
    ans = max_length_subarray(nums=nums, target=target)
    print(ans)
