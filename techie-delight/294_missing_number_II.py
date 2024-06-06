'''

Given an integer array of size `n` and containing elements between 1 and `n+1` with one element missing, find the missing number using constant space.

Input: [3, 2, 4, 6, 1]
Output: 5

Input: [3, 2, 4, 5, 6]
Output: 1

Input: [3, 2, 4, 5, 1]
Output: 6

Assume valid input.

Hint: user XOR (bitwise exclusive OR) operation
The reason this works is that the XOR operation has the following properties:
a ^ 0 = a
a ^ a = 0
a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

'''

from typing import List

def find_missing_number(nums: List[int]):
    n = len(nums) + 1
    xor_sum = 0

    for num in nums:
        xor_sum = xor_sum ^ num
    
    for i in range(1, n+1):
        xor_sum = xor_sum ^ i

    return xor_sum

if __name__=="__main__":
    nums = [3, 2, 4, 5, 1]
    ans = find_missing_number(nums)
    print(ans)