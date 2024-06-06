'''

Given two sequences, find the length of the longest common subsequence (LCS) present in it. The LCS is the longest sequence which can be obtained from the first sequence by deleting some items and from the second sequence by deleting other items.

Input: X = 'ABCBDAB', Y = 'BDCABA'
Output: 4
Explanation: The LCS are 'BDAB', 'BCAB', and 'BCBA', having length 4.

'''

def find_lcs_length(X: str, Y: str) -> int:
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__=="__main__":
    X = 'ABCBDAB'
    Y = 'BDCABA'
    ans = find_lcs_length(X, Y)
    print(ans)