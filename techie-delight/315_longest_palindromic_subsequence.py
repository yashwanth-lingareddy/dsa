'''

Given a sequence, find the longest subsequences of it that is also a palindrome.

Input: 'ABBDCACB'
Output: 5
Explanation: The longest palindromic subsequence is 'BCACB', having length 5.

'''

def find_lps_length(s: str):
    n = len(s)
    reversed_s = s[::-1]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == reversed_s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lps = ""
    i, j = n, n
    while i > 0 and j > 0:
        if s[i - 1] == reversed_s[j - 1]:
            lps = s[i - 1] + lps
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return len(lps)

if __name__=="__main__":
    s = 'ABBDCACB'
    ans = find_lps_length(s)
    print(ans)