'''

Given an integer array `A`, find the peak element in it. An element `A[i]` is a peak element if it's greater than its neighbor(s). i.e.,

• A[i-1] <= A[i] >= A[i+1]	(for 0 < i < n-1)
• A[i-1] <= A[i]			(if i = n – 1)
• A[i] >= A[i+1]			(if i = 0)


Input: [8, 9, 10, 12, 15]
Output: 15

Input: [10, 8, 6, 5, 3, 2]
Output: 10

• There might be multiple peak elements in an array, the solution should report any peak element.

Input: [8, 9, 10, 2, 5, 6]
Output: 10 or 6

Input: [8, 9, 2, 5, 6, 3]
Output: 9 or 6

• If the peak element is not located, the procedure should return -1.

Input: []
Output: -1
'''
from typing import List

def find_peak_element(nums: List[int]) -> int:
    # Write your code here...
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 1
    peak_elements = []
    for i in range(len(nums)):
        if i == 0:
            if nums[i] >= nums[i + 1]:
                peak_elements.append(nums[i])
            continue
        if i == len(nums) - 1:
            if nums[i - 1] <= nums[i]:
                peak_elements.append(nums[i])
            continue
        if nums[i - 1] <= nums[i] and nums[i] >= nums[i + 1]:
            peak_elements.append(nums[i])
        
    if len(peak_elements) == 0:
        return -1
    return peak_elements[0]

if __name__=="__main__":
    nums = [8, 9, 10, 12, 15]
    ans = find_peak_element(nums=nums)
    print(ans)