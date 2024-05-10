'''

Given an integer array, find the largest contiguous subarray formed by consecutive integers. The subarray should contain all distinct values.

Input : [2, 0, 2, 1, 4, 3, 1, 0]
Output: [0, 2, 1, 4, 3]

In case the multiple consecutive subarrays of maximum length exists, the solution can return any one of them.

Input : [-5, -1, 0, 2, 1, 6, 5, 8, 7]
Output: [-1, 0, 2, 1] or [6, 5, 8, 7]

Solution:
Hint: If any array has elements that can be arranged in a continuous sequence, then
    - all the elements in the array should be distinct
    - difference between largest and smallest of the array will always be equal to difference between end index and start index of the array

So, a contiguous subarray is a subarray where
    - all the elements in the subarray is distinct
    - difference between largest and smallest of subarray is equal to difference between end index and start index of subarray
'''

from typing import List

def largest_contiguous_subarray(nums: List[int]):
    contiguous_subarray = []
    for i in range(len(nums)):
        element_set = set()
        element_set.add(nums[i])
        min_element = nums[i]
        max_element = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] in element_set:
                break
            min_element = min(min_element, nums[j])
            max_element = max(max_element, nums[j])

            if max_element - min_element == j - i:
                length_of_this_contiguous_subarray = j - i + 1
                if length_of_this_contiguous_subarray > len(contiguous_subarray):
                    contiguous_subarray = nums[i:j+1]
    
    # edge case if no contiguous_subarray
    # like if input is [1, 3, 5, 7, 9]
    # then array with just first element
    if len(contiguous_subarray) == 0:
        return nums[0:1]

    return contiguous_subarray


if __name__=="__main__":
    nums = [1, 3, 5, 7, 9]
    ans = largest_contiguous_subarray(nums=nums)
    print(ans)