'''

Given a set S, return all distinct subsets of it, i.e., find distinct power set of set S. A power set of any set S is the set of all subsets of S, including the empty set and S itself.

Input : S[] = [1, 2, 3]
Output: [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]

Input : S[] = [1, 2, 1]
Output: [[1, 1, 2], [1, 2], [2], [1, 1], [1], []]

Input : S[] = [1, 1]
Output: [[1, 1], [1], []]

Input : S[] = []
Output: [[]]

Note: The solution can return elements of a subsets in any order and Power sets should contain unique subsets.

'''

from typing import List, Set

def back_track(S: List[int], start: int, current_subset: List[int], complete: Set[str]):
    if start < 0 or start > len(S):
        return

    this_subset = current_subset[:]
    this_subset.sort()
    if len(this_subset) == 0:
        complete.add('')
    else:
        complete.add(''.join(str(num) for num in this_subset))
    for i in range(start, len(S)):
        current_subset.append(S[i])
        back_track(S, i + 1, current_subset, complete)
        current_subset.pop()

def get_power_sets(S: List[int]):
    powerset = []
    if len(S) == 0:
        return [[]]
    complete = set()
    # Write your code here...
    if len(S) == 0:
        return powerset
    back_track(S, 0, [], complete)
    for s in complete:
        if s == "":
            powerset.append([])
        else:
            powerset.append([int(c) for c in s])
    return powerset

if __name__=="__main__":
    S = [1, 2, 3]
    ans = get_power_sets(S=S)
    print(ans)
