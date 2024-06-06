'''

Given a sequence, find the length of the longest subsequence of it that occurs at least twice where the repeated characters should holds a different index in the sequence.

Input: 'ATACTCGGA'
Output: 4
Explanation: The longest repeating subsequence is 'ATCG', having length 4.

'A' 'T'  A  'C'  T   C  'G'  G   A
 A   T  'A'  C  'T' 'C'  G  'G'  A

Input: 'YBYXBXBB'
Output: 5
Explanation: The longest repeating subsequence is 'YBXBB', having length 5.

'Y' 'B'  Y  'X' 'B'  X  'B'  B
 Y   B  'Y'  X  'B' 'X' 'B' 'B'

'''

def find_lrs_length(s: str):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]

if __name__=="__main__":
    s = 'ATACTCGGA'
    ans = find_lrs_length(s)
    print(ans)