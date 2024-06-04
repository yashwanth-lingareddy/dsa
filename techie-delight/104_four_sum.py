'''

Given an unsorted integer array, find all quadruplets (i.e., four elements tuple) having a given sum.

Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 7
Output: {(0, 1, 2, 4)}

Since the input can contain multiple quadruplets that sum to a given target, the solution should return a set containing all the quadruplets.

Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 20
Output: {(0, 4, 7, 9), (1, 3, 7, 9), (2, 4, 5, 9)}

Note: The order of elements doesn't matter in a quadruplet, and any permutation is allowed in the output. For example, the output set can contain quadruplets [9, 1, 7, 3] and [9, 3, 7, 1], but system treats them the same.

ToDo: Look for any optimal solutions

'''
from typing import List, Tuple, Set

def find_quadrapulets(nums: List[int], target: int) -> Set[Tuple[int]]:
    quadruplets = set()
    # Write your code here...
    complement_set = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                this_sum = nums[i] + nums[j] + nums[k]
                complement = target - this_sum
                if complement in complement_set:
                    quadruplets.add(tuple([nums[i], nums[j], nums[k], complement]))
        complement_set.add(nums[i])
    return quadruplets

if __name__=="__main__":
    nums = [2, 7, 4, 0, 9, 5, 1, 3] 
    target = 20
    ans = find_quadrapulets(nums=nums, target=target)
    print(ans)