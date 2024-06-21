'''

Given an array of distinct integers, in-place replace each array element by its corresponding rank in the array. The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on.

Input : [10, 8, 15, 12, 6, 20, 1]
Output: [4, 3, 6, 5, 2, 7, 1]

Input : [0, 1, -1]
Output: [2, 3, 1]

'''

import heapq

from typing import List

def replace_with_rank(nums: List[int]):
    element_rank = {n: 0 for n in nums}
    rank = 0
    heapq.heapify(nums)
    while len(nums) > 0:
        element = heapq.heappop(nums)
        rank += 1
        element_rank[element] = rank
    
    for k, v in element_rank.items():
        nums.append(v)
    
    return

if __name__=="__main__":
    nums = [10, 8, 15, 12, 6, 20, 1]
    replace_with_rank(nums=nums)
    print(nums)