'''
Question:
Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

Input : [1, 1, 1, 0, 0, 1, 1]
Output: [0, 0, 0, 1, 1, 1]
'''
from typing import List

def sort_array(nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1

    while (l < r):
        if nums[l] == 0:
            l+=1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            r-=1
    
    return nums

if __name__=="__main__":
    nums = [1, 1, 1, 0, 0, 1, 1]
    ans = sort_array(nums=nums)
    print(ans)
