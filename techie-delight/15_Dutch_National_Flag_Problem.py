'''

Given an array containing only 0’s, 1’s, and 2’s, in-place sort it in linear time and using constant space.

Input : [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

'''
from typing import List

def sort_array(nums: List[int]):
    zerosCount = 0
    onesCount = 0
    twosCount = 0
    for n in nums:
        if n == 0:
            zerosCount += 1
        if n == 1:
            onesCount += 1
        if n == 2:
            twosCount += 1
    for i in range(zerosCount):
        nums[i] = 0
    
    for i in range(zerosCount, zerosCount + onesCount):
        nums[i] = 1
    
    for i in range(zerosCount + onesCount, zerosCount + onesCount + twosCount):
        nums[i] = 2

if __name__=="__main__":
    nums = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    sort_array(nums=nums)
    print(nums)
