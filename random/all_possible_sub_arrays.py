'''
Given an array return all possible sub arrays
'''
from typing import List

def back_track(arr: List[int], start: int, sub_array: List[int], all_sub_arrays: List[List[int]]):
    if start > len(arr):
        return
    all_sub_arrays.append(sub_array[:])
    for i in range(start, len(arr)):
        sub_array.append(arr[i])
        back_track(arr, i + 1, sub_array, all_sub_arrays)
        sub_array.pop()

def get_all_sub_arrays(arr: List[int]):
    all_sub_arrays = []
    sub_array = []
    back_track(arr, 0, sub_array, all_sub_arrays)
    return all_sub_arrays

if __name__=="__main__":
    arr = [1,2,3,4]
    ans = get_all_sub_arrays(arr)
    print(ans)