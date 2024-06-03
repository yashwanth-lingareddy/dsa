'''

Given an unsorted integer array, find a triplet with a given sum `k` in it.

Input : [4, -1, 1, 2, -1], k = 0
Output: (-1, 2, -1)

Input : [4, 5, 4, -1, 3], k = 10
Output: ()
Explanation: No triplet exists with sum 10.

If the input contains several triplets with sum `k`, the solution can return any one of them.

Input : nums[] = [2, 7, 4, 0, 9, 5, 1, 3], k = 6
Output: (0, 1, 5) or (0, 2, 4) or (1, 2, 3)

Note: The solution can return the triplet in any order, not necessarily as they appear in the array.

'''

from typing import List, Tuple

def find_triplets(nums: List[int], k: int) -> Tuple[int]:
    complement_set = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            this_sum = nums[i] + nums[j]
            complement = k - this_sum
            if complement in complement_set:
                return tuple([nums[i], nums[j], complement])
        complement_set.add(nums[i])
    return tuple([])

if __name__=="__main__":
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    k = 6
    ans = find_triplets(nums, k)
    print(ans)
