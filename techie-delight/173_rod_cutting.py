'''

Given a rod of length `n` and a list of rod prices of length `i`, where `1 <= i <= n`, find the optimal way to cut the rod into smaller rods to maximize profit.

Input:

n = 4 									(Rod length)
price = [1, 5, 8, 9, 10, 17, 17, 20]	(Rod of length `i` has a cost price[i-1])

Output: 10
Explanation: Cut the rod into two pieces of length 2 each to gain revenue of 5 + 5 = 10

Cut		  		Profit

4				9
1, 3			(1 + 8) = 9
2, 2			(5 + 5) = 10	  <-- optimal way
3, 1			(8 + 1) = 9
1, 1, 2			(1 + 1 + 5) = 7
1, 2, 1			(1 + 5 + 1) = 7
2, 1, 1			(5 + 1 + 1) = 7
1, 1, 1, 1		(1 + 1 + 1 + 1) = 4

'''

from typing import List

def max_profit(price: List[int], n: int):
    if n == 0:
        return 0
    max_revenue = price[n-1]
    for i in range(1, n):
        max_revenue = max(max_revenue, price[i-1] + max_profit(price, n - i))
    
    return max_revenue

if __name__=="__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4
    ans = max_profit(price, n)
    print(ans)