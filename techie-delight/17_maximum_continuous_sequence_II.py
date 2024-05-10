'''

Given a binary array and a positive integer `k`, return the indices of the maximum sequence of continuous 1’s that can be formed by replacing at most `k` zeroes by ones.

• The solution should return a pair of the starting and the ending index of the maximum sequence.
• For invalid inputs, the solution should return an empty tuple.
• In case multiple sequence of continuous 1’s of maximum length exists, the solution can return any one of them.

Input : nums[] = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0], k = 0
Output: (6, 9)
Explanation: The longest sequence of continuous 1’s is formed by index 6 to 9.

Input : nums[] = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0], k = 1
Output: (3, 9)
Explanation: The longest sequence of continuous 1’s is formed by index 3 to 9 on replacing zero at index 5.

Input : nums[] = [1, 1, 1, 1, 1], k = 1
Output: (0, 4)

Input : nums[] = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1], k = 1
Output: (0, 3) or (6, 9)

Input : nums[] = [], k = 1
Output: ()

'''
from typing import List

def longest_sequence(nums: List[int], k: int):
    if len(nums) <= 0:
        return tuple([])
    if 0 not in nums:
        return tuple([0, len(nums) - 1])
    start_index_of_longest_sequence = -1
    end_index_of_longest_sequence = -1
    i = 0
    max_length_of_longest_sequence = 0
    while i < len(nums):
        start_index_of_window = i
        end_index_of_window = i
        zeros_count_in_this_window = 0
        index_of_first_zero = -1
        while end_index_of_window < len(nums):
            if nums[end_index_of_window] == 0:
                zeros_count_in_this_window += 1
                if zeros_count_in_this_window == 1:
                    index_of_first_zero = end_index_of_window
                if zeros_count_in_this_window > k:
                    break
            end_index_of_window += 1
        
        this_window = nums[start_index_of_window:(end_index_of_window - 1) + 1]
        if len(this_window) > max_length_of_longest_sequence:
            max_length_of_longest_sequence = len(this_window)
            start_index_of_longest_sequence = start_index_of_window
            end_index_of_longest_sequence = end_index_of_window - 1
        
        if index_of_first_zero == -1:
            break
        i = index_of_first_zero + 1

    return tuple([start_index_of_longest_sequence, end_index_of_longest_sequence])

if __name__=="__main__":

    nums = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
    k = 1
    ans = longest_sequence(nums=nums, k=k)
    print(ans)