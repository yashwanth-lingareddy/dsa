'''

Given an integer array, return all equilibrium index in it. For an array `A[0..n-1]`, index `i` is an equilibrium index if the sum of elements of subarray `A[0…i-1]` is equal to the sum of elements of subarray `A[i+1…n-1]`.

Input : [0, -3, 5, -4, -2, 3, 1, 0]
Output: {0, 3, 7}
Explanation: For each index `i` in the output, A[0] + A[1] + … + A[i-1] = A[i+1] + A[i+2] + … + A[n-1]

Input : [-7, 3, 7, -3, 1]
Output: {4}
Explanation: `n-1` is an equilibrium index if A[0] + A[1] + … + A[n-2] sums to 0.

Input : [1, 2, -4, 2]
Output: {0}
Explanation: 0 is an equilibrium index if A[1] + A[2] + … + A[n-1] sums to 0.

Solution
1. Find total sum of the array
2. Iterate from left to right
3. For each element get the left sum by cummulative sum
4. Right sum = total sum - left sum
5. For each element sum of nums left of that element will be left_sum - current_element
6. For each element sum of nums right of that element will be right_sum - current_element
5. If left of the element is equal to right of the element, then it is equilibrium index
'''
from typing import List

def equilibrium_indexes(nums: List[int]):
    total_sum = 0
    left_sum = 0
    equ_indexes = set()

    for n in nums:
        total_sum += n

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            equ_indexes.add(i)
        left_sum += nums[i]
    
    return equ_indexes

if __name__=="__main__":
    nums = [0, -3, 5, -4, -2, 3, 1, 0]
    ans = equilibrium_indexes(nums=nums)
    print(ans)
