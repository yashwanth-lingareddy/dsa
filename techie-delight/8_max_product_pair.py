'''
Question:
Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

Solution
Max product is always equal two largest positive numbers or two smallest negative numbers
'''
import sys
from typing import List, Tuple

def find_max_product_pair(nums: List[int]) -> Tuple[int]:
    # edge case
    # we can get pair only if length is >= 2
    if len(nums) < 2:
        return ()
    first_largest_number = sys.maxsize * -1
    second_largest_number = sys.maxsize * -1
    for n in nums:
        if n > first_largest_number:
            first_largest_number = n

    for n in nums:
        if n == first_largest_number:
            continue
        if n > second_largest_number:
            second_largest_number = n
    
    if second_largest_number == sys.maxsize * -1:
        second_largest_number = first_largest_number

    first_smallest_number = sys.maxsize
    second_smallest_number = sys.maxsize
    
    for n in nums:
        if n < first_smallest_number:
            first_smallest_number = n
    
    for n in nums:
        if n == first_smallest_number:
            continue
        if n < second_smallest_number:
            second_smallest_number = n

    if second_smallest_number == sys.maxsize:
        second_smallest_number = first_smallest_number
    
    ans = tuple([first_largest_number, second_largest_number])
    p1 = first_largest_number * second_largest_number
    p2 = first_smallest_number * second_smallest_number

    print(first_largest_number, second_largest_number)
    print(first_smallest_number, second_smallest_number)

    if p2 > p1:
        ans = tuple([first_smallest_number, second_smallest_number])
    return ans

if __name__=="__main__":
    nums = [-5,-4]
    # nums = [-4, 3, 2, 7, -5]
    ans = find_max_product_pair(nums=nums)
    print(ans)