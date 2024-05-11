'''

Given an integer array, in-place replace each element with the product of every other element without using the division operator.

Input : [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]

Input : [5, 3, 4, 2, 6, 8]
Output: [1152, 1920, 1440, 2880, 960, 720]

'''
from typing import List

def replace_elements(nums: List[int]):
    prefix_product = 1
    temp = [n for n in nums]

    for i in range(len(nums)):
        nums[i] = prefix_product
        prefix_product *= temp[i]

    suffix_product = 1
    for i in range(len(nums) - 1, -1, -1):
        nums[i] *= suffix_product
        suffix_product *= temp[i]

if __name__=="__main__":
    nums = [1, 2, 3, 4, 5]
    replace_elements(nums=nums)
    print(nums)
