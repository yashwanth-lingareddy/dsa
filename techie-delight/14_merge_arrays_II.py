'''

Given two sorted integer arrays `X[]` and `Y[]` of size `m` and `n` each where `m >= n` and `X[]` has exactly `n` vacant cells, merge elements of `Y[]` in their correct position in array `X[]`, i.e., merge `(X, Y)` by keeping the sorted order.

Input : Two arrays X[] and Y[] where vacant cells in X[] is represented by 0.

X[] = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y[] = [1, 8, 9, 10, 15]

Output: X[] = [1, 2, 3, 5, 6, 8, 9, 10, 15]

Solution:
1. Move all non zero elements of the array to the end. [0, 2, 0, 3, 0, 5, 6, 0, 0] will become [0, 0, 0, 0, 0, 2, 3, 5, 6]
2. Start two pointers i, j where i is first non zero element of X and j is first element of Y
3. if element in X is greater than Y, swap element of X at index i with element of Y at index j, increment index j
4. Else swap element of X at index i with first first zero element of X, increment index i 

'''
from typing import List

def move_non_zero_elements_to_the_end(nums: List[int]):
    i = len(nums) - 1
    j = len(nums) - 1
    while i >= 0:
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i -= 1

def merge_arrays(X: List[int], Y: List[int]):
    if len(X) == 0 or len(Y) == 0:
        return
    move_non_zero_elements_to_the_end(X)
    # start at first non zero element of X and compare it with Y
    # let i be the index of first non zero element of X
    # let j be the first index of Y
    # let k be index to keep track of position of array
    i = len(Y) # first non zero element index of X will always be equal to length of Y
    j = 0
    k = 0
    while i < len(X) and j < len(Y):
        if Y[j] < X[i]:
            X[k], Y[j] = Y[j], X[k]
            j += 1
        else:
            X[k], X[i] = X[i], X[k]
            i += 1
        k += 1
    # Replaces all the remaing zeros of X with Y elements
    i = len(X) - 1
    j = len(Y) - 1

    while Y[j] != 0 and j >= 0:
        X[i], Y[j] = Y[j], X[i]
        j -= 1
        i -= 1

if __name__ == "__main__":
    X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    Y = [1, 8, 9, 10, 15]
    merge_arrays(X, Y)
    print(X)
