'''

Given two words, find the minimum number of single-character edits required to transform one word into the other. An edit can be insertion, deletion, or substitution and each edit carries a unit cost.

Input: X = 'kitten', Y = 'sitting'
Output: 3
Explanation: A minimal edit script that transforms the 'kitten' into 'sitting' is:

kitten —> sitten (substitution of 's' for 'k')
sitten —> sittin (substitution of 'i' for 'e')
sittin —> sitting (insertion of 'g' at the end)

'''

def find_min_distance(X: str, Y: str):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

if __name__=="__main__":
    X = 'kitten'
    Y = 'sitting'
    ans = find_min_distance(X, Y)
    print(ans)