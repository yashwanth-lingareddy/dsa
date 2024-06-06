'''

Given a set of positive integers, check if it can be divided into two subsets with equal sum.

Input: S = [3, 1, 1, 2, 2, 1]
Output: True
Explanation: S can be partitioned into two partitions, each having a sum of 5.

S1 = [1, 1, 1, 2]
S2 = [2, 3]

Note that this solution is not unique. Here’s another solution.

S1 = [3, 1, 1]
S2 = [2, 2, 1]

'''

from typing import List

def partition(nums: List[int]):
    n = len(nums)
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    
    return dp[n][target_sum]

if __name__=="__main__":
    S = [3, 1, 1, 2, 2, 1]
    ans = partition(S)
    print(ans)