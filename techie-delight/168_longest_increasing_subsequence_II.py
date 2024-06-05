'''

Given a given sequence, find the longest increasing subsequence (LIS) in it.

The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible.

The longest increasing subsequence is not necessarily unique, the solution can return any valid subsequence.

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output: [0, 2, 6, 9, 11, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

'''

from typing import List

def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1
    prev = [-1] * n  # Store the previous index for each element in the LIS

    max_len = 1
    max_idx = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i

    # Reconstruct the LIS using the prev array
    lis = []
    while max_idx != -1:
        lis.append(nums[max_idx])
        max_idx = prev[max_idx]

    return lis[::-1]  # Reverse the list to get the LIS in the correct order

if __name__=="__main__":
    nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    ans = longest_increasing_subsequence(nums)
    print(ans)