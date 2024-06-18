'''

Given an integer array, find k'th largest element in the array where k is a positive integer less than or equal to the length of array.

Input : [7, 4, 6, 3, 9, 1], k = 2
Output: 7
Explanation: The 2nd largest array element is 7

Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 4
Output: 4
Explanation: The 4th largest array element is 4

ToDo: this can also be done using min heap
- Create a min heap of size k and insert the first k elements of the array into the heap.
- For the remaining (n-k) elements, compare each element with the root (minimum element) of the heap.
- If the element is greater than the root, remove the root and insert the new element into the heap.
- After processing all elements, the root of the heap will be the k'th largest element.
- Time Complexity: O(n log k)
- Space Complexity: O(k) for the heap
'''
import heapq
from typing import List

def kth_largest_element(nums: List[int], k: int):
    nums.sort()
    return nums[len(nums) - k]

def kth_latgest_element_using_heap(nums: List[int], k: int):
    # create a heap with first k elements of the array
    heap = [x for x in nums[:k]]
    heapq.heapify(heap)

    # iterate the remainin elements of the array, which is (n - k)
    for n in nums[k:]:
        # if the element is greatter than first item in the heap
        # then remove the first item in the heap
        # and insert this element to the heap
        if n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)
    
    return heap[0]

if __name__=="__main__":
    nums = [1, 5, 2, 2, 2, 5, 5, 4]
    k = 4
    ans = kth_latgest_element_using_heap(nums=nums, k=k)
    print(ans)