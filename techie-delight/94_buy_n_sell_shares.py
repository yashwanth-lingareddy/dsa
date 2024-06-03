'''

Given a list containing future prediction of share prices, find the maximum profit earned by buying and selling shares any number of times with the constraint, a new transaction can only start after the previous transaction is complete, i.e., you can only hold at most one share at a time.

Input : [1, 5, 2, 3, 7, 6, 4, 5]
Output: 10
Explanation: Total profit earned is 10

Buy on day 1 and sell on day 2
Buy on day 3 and sell on day 5
Buy on day 7 and sell on day 8


Input : [10, 8, 6, 5, 4, 2]
Output: 0

'''

from typing import List

def find_max_profit(price: List[int]):
    profit = 0
    for i in range(1, len(price)):
        if price[i] > price[i-1]:
            profit += (price[i] - price[i-1])
    return profit

if __name__=="__main__":
    price = [1, 5, 2, 3, 7, 6, 4, 5]
    ans = find_max_profit(price)
    print(ans)