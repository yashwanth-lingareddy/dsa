'''

Given an integer array, right-rotate it by `k` positions, where `k` is a postive integer.

Input: nums[] = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: nums[] = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]

Input: nums[] = [1, 2, 3, 4, 5], k = 6
Output: [1, 2, 3, 4, 5]
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
[2, 3, 4, 5, 1]
[1, 2, 3, 4, 5]
'''

from typing import List

def reverse(nums: List[int]):
    i = 0
    j = len(nums) - 1

    while(i < j):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def right_rotate_array(nums: List[int], k: int):
    n = len(nums)
    k = k % n  # Handle cases where k is greater than the length of the array

    # Reverse the entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Reverse the remaining (n-k) elements
    nums[k:] = reversed(nums[k:])

    return nums

if __name__=="__main__":
    nums = [1, 2, 3, 4, 5]
    k = 5
    ans = right_rotate_array(nums=nums, k=k)
    print(ans)