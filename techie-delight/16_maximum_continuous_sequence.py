'''

Given a binary array, find the index of 0 to be replaced with 1 to get the maximum length sequence of continuous ones. The solution should return the index of first occurence of 0, when multiple continuous sequence of maximum length is possible.

Input : [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
Output: 7
Explanation: Replace index 7 to get the continuous sequence of length 6 containing all 1’s.

Input : [0, 1, 1, 0, 0]
Output: 0
Explanation: Replace index 0 or 3 to get the continuous sequence of length 3 containing all 1’s. The solution should return the first occurence.

Input : [1, 1]
Output: -1
Explanation: Invalid Input (all 1’s)

Solution:
Sliding Window
Start a window and keep expanding the window until there is only one zero and all ones
If second zero enters window break the window
Keep track of largest window so far
In the largest window return the index of 0
'''
from typing import List

def find_index_of_zero(nums: List[int]):
    if 0 not in nums:
        return -1
    i = 0
    start_index_of_window = -1
    largest_window_length = 0
    index_of_zero_to_be_replaced = -1
    while i < len(nums):
        start_index_of_window = i
        end_index_of_window = i
        zeros_in_this_window = 0
        index_of_first_zero_in_this_window = -1
        index_of_second_zero_in_this_window = -1
        while end_index_of_window < len(nums):
            if nums[end_index_of_window] == 0:
                zeros_in_this_window += 1
                if zeros_in_this_window == 1:
                    index_of_first_zero_in_this_window = end_index_of_window
                if zeros_in_this_window == 2:
                    index_of_second_zero_in_this_window = end_index_of_window
                    break
            end_index_of_window += 1
        this_window = nums[start_index_of_window:(end_index_of_window - 1) + 1]
        if len(this_window) > largest_window_length:
            largest_window_length = len(this_window)
            index_of_zero_to_be_replaced = index_of_first_zero_in_this_window
        if index_of_first_zero_in_this_window == -1:
            break
        i = index_of_first_zero_in_this_window + 1

    return index_of_zero_to_be_replaced

if __name__=="__main__":
    nums = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    ans = find_index_of_zero(nums=nums)
    print(ans)
    