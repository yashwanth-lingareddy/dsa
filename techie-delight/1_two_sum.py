'''
Question:
Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()


'''
from typing import List, Tuple

def find_pair(nums: List[int], target: int) -> Tuple[int]:
    num_set = set()
    for n in nums:
        complement = target - n
        if complement in num_set:
            return tuple([n, complement])
        else:
            num_set.add(n)

if __name__=="__main__":
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    ans = find_pair(nums=nums, target=target)
    print(ans)
