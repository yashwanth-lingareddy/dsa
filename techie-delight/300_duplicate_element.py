'''

Given an integer array of size `n` containing elements between 1 and `n-1` with one element repeating, find the duplicate number in it using constant space.

Input: [1, 2, 3, 4, 4]
Output: 4

Input: [1, 2, 3, 4, 2]
Output: 2

Input: [1, 1]
Output: 1

Assume valid input.

'''

from typing import List

def find_duplicate_element(nums: List[int]):
    # Write your code here...
    # Initialize slow and fast pointers
    slow = nums[0]
    fast = nums[0]

    # Find the meeting point of slow and fast pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset slow to the start of the array
    slow = nums[0]

    # Find the start of the cycle
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # The start of the cycle is the duplicate number
    return slow

if __name__=="__main__":
    nums = [1, 2, 3, 4, 4]
    ans =find_duplicate_element(nums)
    print(ans)