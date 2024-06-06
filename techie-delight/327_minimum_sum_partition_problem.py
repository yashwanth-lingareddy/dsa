'''

Given a set of positive integers S, partition it into two subsets, S1 and S2, such that the difference between the sum of elements in S1 and S2 is mininum. The solution should return the minimum absolute difference between the sum of elements of two partitions.

Input: S = [10, 20, 15, 5, 25]
Output: 5
Explanation: S can be partitioned into two partitions [[10, 20, 5], [15, 25]] where the minimum absolute difference between the sum of elements is 5. Note that this solution is not unique. Another solution is [[10, 25], [20, 15, 5]].

Input: []
Output: 0

'''
from typing import List

def find_min_abs_distance(S: List[int]):
    n = len(S)
    total_sum = sum(S)
    
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if S[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]
    
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            s1 = j
            break
    
    return abs(total_sum - 2 * s1)

if __name__=="__main__":
    S = [10, 20, 15, 5, 25]
    ans = find_min_abs_distance(S)
    print(ans)