'''

Given a word and a pattern containing wildcard characters '*' and '?', check if the pattern matches with the complete string or not. Here, '?' can match to any single character in the string and '*' can match to any number of characters including zero characters.

Input: word = 'xyxzzxy', pattern = 'x***y'
Output: True

Input: word = 'xyxzzxy', pattern = 'x***x'
Output: False

Input: Input: word = 'xyxzzxy', pattern = '*'
Output: True

Input: word = 'xyxzzxy', pattern = '*'
Output: True

'''

def is_matching(word: str, pattern: str):
    n, m = len(word), len(pattern)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] and pattern[j - 1] == '*'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word[i - 1] == pattern[j - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[n][m]

if __name__=="__main__":
    word = 'xyxzzxy'
    pattern = '*'
    ans = is_matching(word=word, pattern=pattern)
    print(ans)