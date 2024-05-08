'''
Question:
Given a binary array containing 0’s and 1’s, find the largest contiguous subarray with equal numbers of 0’s and 1’s.

Input : [0, 0, 1, 0, 1, 0, 0]
Output: [0, 1, 0, 1] or [1, 0, 1, 0]

Input : [0, 0, 0, 0]
Output: []

Note: Since an input can contain several largest subarrays with equal numbers of 0’s and 1’s, the code should return any one of them.

Solution: Replace all 0's with -1
then this problem will become largest subarray with sum equal to 0
'''
from typing import List

def find_largest_subarray(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1
    target = 0
    prefix_sum = 0
    prefix_sum_index_map = {0:[-1]}
    max_length_subarray = []

    for i in range(len(nums)):
        this_number = nums[i]
        prefix_sum += this_number
        this_subarray = []

        if prefix_sum == target:
            this_subarray = nums[0:i+1]
        
        complement = prefix_sum - target

        if complement in prefix_sum_index_map:
            start_index = prefix_sum_index_map[complement][0] + 1
            this_subarray = nums[start_index:i+1]

        prefix_sum_index_map[prefix_sum] = prefix_sum_index_map.get(prefix_sum, []) + [i]

        if len(this_subarray) > len(max_length_subarray):
            max_length_subarray = this_subarray
    
    for i in range(len(max_length_subarray)):
        if max_length_subarray[i] == -1:
            max_length_subarray[i] = 0

    return max_length_subarray


if __name__=="__main__":
    nums = [0, 0, 1, 0, 1, 0, 0]
    ans = find_largest_subarray(nums=nums)
    print(ans)