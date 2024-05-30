'''

Given a positive integer `n`, find all combinations of numbers between 1 and `n` having sum `n`.

Input : n = 4
Output: {(4), (1, 3), (2, 2), (1, 1, 2), (1, 1, 1, 1)}

Input : n = 5
Output: {(5), (1, 4), (2, 3), (1, 1, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)}

The solution should return a set containing all the distinct combinations in increasing order.
'''

from typing import List, Set, Tuple

def back_track(n: int, start: int, combination: List[int], target: int, result: Set[Tuple[int]]):
    if target == 0:
        result.add(tuple(combination))
        return

    for i in range(start, n + 1):
        if i > target:
            break
        combination.append(i)
        back_track(n, i, combination, target - i, result)
        combination.pop()

def find_combinations(n: int):
    result = set()
    back_track(n, 1, [], n, result)
    return result

# Example usage
n = 5
combinations = find_combinations(n)
print(combinations)