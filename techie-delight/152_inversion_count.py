'''

Given an integer array, find the total number of inversions of it. If `(i < j)` and `(nums[i] > nums[j])`, then pair `(i, j)` is called an inversion of an array `nums`. The solution should provide count of all such pairs in the array.

Input : [1, 9, 6, 4, 5]
Output: 5
Explanation: There are 5 inversions in the array: (9, 6), (9, 4), (9, 5), (6, 4), (6, 5)

'''

from typing import List

def is_inverted_array(i, j, nums):
    return i < j and nums[i] > nums[j]

def back_track(nums: List[int], start: int, this_array: List[int], this_index: List[int], sub_arrays: List[List[int]], indexes: List[List[int]], inverted_arrays: List[List[int]]):
    if start > len(nums):
        return
    if len(this_array) == 2:
        first_index = this_index[0]
        second_index = this_index[1]
        if is_inverted_array(first_index, second_index, nums):
            inverted_arrays.append(this_array[:])
        sub_arrays.append(this_array[:])
        indexes.append(this_index[:])
    for i in range(start, len(nums)):
        this_array.append(nums[i])
        this_index.append(i)
        back_track(nums, i+1, this_array, this_index, sub_arrays, indexes, inverted_arrays)
        this_array.pop()
        this_index.pop()

def sub_arrays(nums: List[int]):
    sub_arrays = []
    indexes = []
    inverted_arrays = []
    back_track(nums, 0, [], [], sub_arrays, indexes, inverted_arrays)
    return len(inverted_arrays)

if __name__=="__main__":
    nums = [1, 9, 6, 4, 5]
    ans = sub_arrays(nums)
    print(ans)

