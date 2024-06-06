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

from typing import List

def kth_largest_element(nums: List[int], k: int):
    nums.sort()
    return nums[len(nums) - k]

if __name__=="__main__":
    nums = [1, 5, 2, 2, 2, 5, 5, 4]
    k = 4
    ans = kth_largest_element(nums=nums, k=k)
    print(ans)