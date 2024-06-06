'''

Given a set of positive integers and an integer `k`, check if there is any non-empty subset that sums to `k`.

Input: nums = [7, 3, 2, 5, 8], k = 14
Output: True
Explanation: Subset [7, 2, 5] sums to 14

'''

from typing import List

def subset_sum(nums: List[int], k: int):
    n = len(nums)
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if  nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    
    return dp[n][k]

if __name__=="__main__":
    nums = [7, 3, 2, 5, 8]
    k = 14
    ans = subset_sum(nums, k)
    print(ans)