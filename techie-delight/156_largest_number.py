'''

Find the largest number possible from a set of given numbers, where the numbers append to each other in any order to form the largest number. The solution should return the string representation of the largest number.

Input : [10, 68, 75, 7, 21, 12]
Output: 77568211210

'''

from typing import List
from functools import cmp_to_key

def compare(a: str, b: str):
        ab = a + b
        ba = b + a
        if int(ab) > int(ba):
            return -1  # a should come before b
        elif int(ab) < int(ba):
            return 1   # b should come before a
        else:
            return 0   # a and b are equal

def largest_number(nums: List[int]):
    # Convert numbers to strings
    nums = [str(num) for num in nums]
    
    # Sort the strings using the custom comparison function
    sorted_nums = sorted(nums, key=cmp_to_key(compare))

    # Concatenate the sorted strings
    largest_num = ''.join(sorted_nums)

    # Handle the case where the largest number starts with '0'
    return '0' if largest_num[0] == '0' else largest_num

if __name__=="__main__":
    nums = [10, 68, 75, 7, 21, 12]
    ans = largest_number(nums)
    print(ans)