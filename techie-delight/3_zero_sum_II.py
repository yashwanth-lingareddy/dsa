'''
Question:
Given an integer array, find all contiguous subarrays with zero-sum.

Input : [4, 2, -3, -1, 0, 4]
Output: {(0), (-3, -1, 0, 4)}

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: {(3, 4, -7, 3, 1, 3, 1, -4, -2, -2), (3, 4, -7), (3, 1, 3, 1, -4, -2, -2), (3, 1, -4), (-7, 3, 1, 3), (4, -7, 3)}

Input : [0, 0]
Output: {(0), (0, 0)}

Input : [1, 2, 3]
Output: {}

Note: Since an input can have multiple subarrays with zero-sum, the solution should return a set of tuples containing all the distinct subarrays.

Answer:
This problem is similar to finding a contiguous subarray having sum equal to a target value,
here the target is 0
Collect all the subarrays having sum equal to a target value
'''
from typing import List, Set, Tuple

def get_all_zero_sum_subarrays(nums: List[int]) -> Set[Tuple[int]]:
    ans = set()
    prefix_sum = 0
    prefix_index = {0:-1}
    target = 0

    for i in range(len(nums)):
        this_num = nums[i]
        prefix_sum += this_num

        if prefix_sum == target:
            ans.add(tuple(nums[0:i+1]))

        complement = prefix_sum - target

        if complement in prefix_index:
            start_index = prefix_index[complement] + 1
            ans.add(tuple(nums[start_index:i+1]))
        
        prefix_index[prefix_sum] = i
    
    return ans


if __name__=="__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    ans = get_all_zero_sum_subarrays(nums=nums)
    print(ans)
