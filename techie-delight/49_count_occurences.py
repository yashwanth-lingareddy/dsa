'''

Given a sorted integer array containing duplicates, return the count of occurrences of a given number.

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 5
Output: 3
Explanation: Target 5 occurs 3 times

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 6
Output: 2
Explanation: Target 6 occurs 2 times

Input: nums[] = [5, 4, 3, 2, 1], target = 6
Output: 0
Explanation: Target 6 occurs 0 times

'''

from typing import List

def count_occrences(nums: List[int], target: int) -> int:
    count = 0
    for n in nums:
        if n > target:
            break
        if n == target:
            count += 1
    return count

if __name__=="__main__":
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 5
    ans = count_occrences(nums, target)
    print(ans)