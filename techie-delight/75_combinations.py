'''

Given an integer array, find all distinct combinations of a given length `k`. The solution should return a set containing all the distinct combinations, while preserving the relative order of elements as they appear in the array.

Input : [2, 3, 4], k = 2
Output: {(2, 3), (2, 4), (3, 4)}

Input : [1, 2, 1], k = 2
Output: {(1, 2), (1, 1), (2, 1)}

Input : [1, 1, 1], k = 2
Output: {(1, 1)}

Input : [1, 2, 3], k = 4
Output: {}

Input : [1, 2], k = 0
Output: {()}

'''

from typing import List, Tuple, Set

def back_track(nums: List[int], k: int, start: int, combination: List[int], result: Set[Tuple[int]]) -> None:
    if len(combination) == k:
        result.add(tuple(combination))
        return

    for i in range(start, len(nums)):
        combination.append(nums[i])
        back_track(nums, k, i + 1, combination, result)
        combination.pop()

def find_combinations(nums: List[int], k: int) -> List[List[int]]:
    result = set()
    if len(nums) == 0:
        return result
    start = 0
    back_track(nums, k, start, [], result)
    return [list(combo) for combo in result]

if __name__=="__main__":
    nums = [2,3,4]
    k = 2
    combinations = find_combinations(nums, k)
    print(combinations)