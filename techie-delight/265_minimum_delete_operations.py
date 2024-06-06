'''

Given a string, find the minimum number of deletions required to convert it into a palindrome.

Input: s = "ACBCDBAA"
Output: 3
Explanation: The minimum number of deletions required to convert "ACBCDBAA" into a palindrome string "ABCBA" is 3.

'''

def find_min_deletions(s: str):
    # Write your code here...
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # Fill the dp table
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # Length of the LPS is dp[0][n-1]
    lps_length = dp[0][n-1]

    # Minimum deletions required = length(s) - length(LPS)
    return n - lps_length

if __name__=="__main__":
    s = "ACBCDBAA"
    ans = find_min_deletions(s)
    print(ans)