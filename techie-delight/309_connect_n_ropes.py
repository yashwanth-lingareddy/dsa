'''

Given n ropes of different lengths, connect them into a single rope with minimum cost. Assume that the cost to connect two ropes is the same as the sum of their lengths.

Input: [5, 4, 2, 8]
Output: 36
Explanation: The total cost for connecting all ropes is 6 + 11 + 19 = 36.

[5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
[5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
[11, 8]      –> Finally, connect the remaining two ropes that will cost 19.

'''

import heapq
from typing import List

def connect_n_ropes(prices: List[int]):
    total_cost = 0
    if not prices:
        return total_cost
    heapq.heapify(prices)
    while len(prices) >= 2:
        cost_to_connect_two_least_ropes = heapq.heappop(prices) + heapq.heappop(prices)
        total_cost += cost_to_connect_two_least_ropes
        heapq.heappush(prices, cost_to_connect_two_least_ropes)
    return total_cost

if __name__=="__main__":
    prices = [5, 4, 2, 8]
    ans = connect_n_ropes(prices=prices)
    print(ans)