'''
Question
Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

Answer:
This problem is similar to finding a contiguous subarray having sum equal to a target value,
here the target is 0
'''
from typing import List

def has_zero_sum_array(nums: List[int]) -> bool:
    target = 0
    prefix_sum = 0
    prefix_index_map = {0:-1}

    for i in range(len(nums)):
        this_num = nums[i]
        prefix_sum += this_num
        complement = prefix_sum - target

        if complement in prefix_index_map:
            # there exists an subarray having sum zero
            return True
        prefix_index_map[prefix_sum] = i
    return False

if __name__=="__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    ans = has_zero_sum_array(nums=nums)
    print(ans)
