'''

Given an integer array, in-place sort it without using any inbuilt functions.

Input : [6, 3, 4, 8, 2, 9]
Output: [2, 3, 4, 6, 8, 9]

Input : [9, -3, 5, -2, -8, -6]
Output: [-8, -6, -3, -2, 5, 9]

'''
import heapq

from typing import List

def heapify(arr: List[int], n: int, i: int):
    """
    Heapify the subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest, swap with the largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def sort_array(nums: List[int]):
    n = len(nums)

    # Build a max heap from the input data
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        nums[i], nums[0] = nums[0], nums[i]

        # Heapify the root element to get the highest element at root again
        heapify(nums, i, 0)


# if this is not in place
def sort_not_in_place(nums: List[int]):
    ans = []
    heapq.heapify(nums) # O(n) complexity
    for i in range(len(nums)):
        ans.append(heapq.heappop(nums))
    
    for n in ans:
        nums.append(n)


def sort_array_v2(nums: List[int]):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                nums[i], nums[j] = nums[j],nums[i]

if __name__=="__main__":
    nums = [6, 3, 4, 8, 2, 9]
    sort_not_in_place(nums=nums)
    print(nums)
