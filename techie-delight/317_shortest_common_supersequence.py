'''

Given two sequences, find the length of the shortest supersequence 'Z' of given sequences 'X' and 'Y' such that both 'X' and 'Y' are subsequences of 'Z'.

Input: X = 'ABCBDAB', Y = 'BDCABA'
Output: 9
Explanation: The SCS are 'ABCBDCABA', 'ABDCABDAB', and 'ABDCBDABA', having length 9.

'''

def find_scs_length(X: str, Y: str):
    m, n = len(X), len(Y)
    
    # Find the length of the longest common subsequence (LCS)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length = dp[m][n]
    
    # Length of the shortest supersequence
    shortest_supersequence_length = m + n - lcs_length
    
    return shortest_supersequence_length

if __name__=="__main__":
    X = 'ABCBDAB'
    Y = 'BDCABA'
    ans = find_scs_length(X, Y)
    print(ans)