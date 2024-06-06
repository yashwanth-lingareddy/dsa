'''

Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. Note that the items are indivisible; we can either take an item or not (0-1 property).

Input:

value = [20, 5, 10, 40, 15, 25]
weight = [1, 2, 3, 8, 7, 4]
int W = 10

Output: 60

Explanation: Knapsack value is 60

value = 20 + 40 = 60
weight = 1 + 8 = 9 <= W

'''
from typing import List

def find_knapsack_value(value: List[int], weight: List[int], W: int) -> int:
    n = len(weight)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weight[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], value[i - 1] + dp[i - 1][j - weight[i - 1]])

    return dp[n][W]

if __name__=="__main__":
    value = [20, 5, 10, 40, 15, 25]
    weight = [1, 2, 3, 8, 7, 4]
    W = 10
    ans = find_knapsack_value(value, weight, W)
    print(ans)

