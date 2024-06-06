'''

Given two strings, find the longest string that is a substring of both strings.

Input: X = 'ABABC', Y = 'BABCA'
Output: 'BABC'
Explanation: The longest common substring of strings 'ABABC' and 'BABCA' is 'BABC' having length 4. The other common substrings are 'ABC', 'A', 'AB', 'B', 'BA', 'BC', and 'C'.

'''

def least_common_substring(X: str, Y: str):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i

    return X[end_index - max_len:end_index]

if __name__=="__main__":
    X = 'ABABC'
    Y = 'BABCA'
    ans = least_common_substring(X, Y)
    print(ans)