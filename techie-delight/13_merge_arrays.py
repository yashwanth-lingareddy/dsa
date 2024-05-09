'''
Question
Given two sorted integer arrays, `X[]` and `Y[]` of size `m` and `n` each, in-place merge elements of `X[]` with elements of array `Y[]` by maintaining the sorted order, i.e., fill `X[]` with the first `m` smallest elements and fill `Y[]` with remaining elements.

Input :

X[] = [1, 4, 7, 8, 10]
Y[] = [2, 3, 9]

Output:

X[] = [1, 2, 3, 4, 7]
Y[] = [8, 9, 10]


Notes: ToDo check if there any optimized solution
'''
from typing import List

def merge(X: List[int], Y: List[int]):
    i = 0
    while i < len(X):
        j = len(Y) - 1
        while j >= 0:
            if X[i] > Y[j]:
                X[i], Y[j] = Y[j], X[i]
            j -= 1
        i += 1
        

if __name__=="__main__":
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]
    merge(X, Y)
    print(X)
    print(Y)