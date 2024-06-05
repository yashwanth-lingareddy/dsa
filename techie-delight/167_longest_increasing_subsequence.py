'''

Given a given sequence, find the length of the longest increasing subsequence (LIS) in it.

The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible.

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output: 6
Explanation: The longest increasing subsequence is [0, 2, 6, 9, 11, 15] having length 6; the input sequence has no 7–member increasing subsequences.

The longest increasing subsequence is not necessarily unique. For instance, [0, 4, 6, 9, 11, 15] and [0, 4, 6, 9, 13, 15] are other increasing subsequences of equal length in the same input sequence.

Hint: This is dynamic progamming problem

'''

from typing import List

def longest_increasing_subarray(nums: List[int]):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__=="__main__":
    nums = [1, 5, 2, 2, 2, 5, 5, 4]
    ans = longest_increasing_subarray(nums)
    print(ans)
    