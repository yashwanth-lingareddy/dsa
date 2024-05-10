'''

Given an integer array of size `n`, return the element which appears more than `n/2` times. Assume that the input always contain the majority element.

Input : [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
Output: 2

Input : [1, 3, 1, 1]
Output: 1

'''
from typing import List

def majority_element(nums: List[int]):
    times_more_than = len(nums) // 2
    element_count = {}
    for n in nums:
        if n not in element_count:
            element_count[n] = 0
        element_count[n] += 1
    
    max_count = 0
    max_count_element = 0
    for k, v in element_count.items():
        if v > max_count and v > times_more_than:
            max_count = v
            max_count_element = k
    return max_count_element

if __name__=="__main__":
    nums = [1, 3, 1, 1]
    ans = majority_element(nums=nums)
    print(ans)