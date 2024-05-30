'''

Given a sorted integer array, find the index of a given number's first and last occurrence.

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 5
Output: (1, 3)
Explanation: The first and last occurrence of element 5 is located at index 1 and 3, respectively.

• If the target is not present in the array, the solution should return the pair (-1, -1).

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 4
Output: (-1, -1)

'''
from typing import List, Tuple

def find_pair(nums: List[int], target: int) -> Tuple[int]:
    first_index = -1
    last_index = -1
    for i in range(0, len(nums)):
        n = nums[i]
        # to not to loop entirely if target is already found
        if n > target:
            break
        if n == target:
            if first_index == -1:
                first_index = i
            
            last_index = i

    return tuple([first_index, last_index])

if __name__=="__main__":
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 5
    ans = find_pair(nums=nums, target=target)
    print(ans)