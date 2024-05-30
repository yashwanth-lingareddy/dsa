'''

Given a circularly sorted array of distinct integers, find the total number of times the array is rotated. You may assume that the rotation is in anti-clockwise direction.

Input: [8, 9, 10, 2, 5, 6]
Output: 3

Input: [2, 5, 6, 8, 9, 10]
Output: 0

Input: [3, 5, 7, 9, 2]
Output: 4

Input: [-6, -9]
Output: 1


Hint: Traverse through the array and find the index at which the direction changes from ascending to descending
The index at which the dierction changes is the rotation_count

'''

from typing import List

def rotation_for_ascending_array(nums: List[int]):
    rotation_count = 0
    for i in range(1, len(nums)):
        prev_element = nums[i - 1]
        this_element = nums[i]
        if this_element < prev_element:
            rotation_count = i
            break
    return rotation_count

def find_rotation_count(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    rotation_count = rotation_for_ascending_array(nums)
    return rotation_count

if __name__ == "__main__":
    nums = [-6, -9]
    ans = find_rotation_count(nums=nums)
    print(ans)
