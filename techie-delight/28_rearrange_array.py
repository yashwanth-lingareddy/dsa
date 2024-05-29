'''

Given an integer array, in-place rearrange it such that every second element becomes greater than its left and right elements.

• Assume that no duplicate elements are present in the input array.
• The solution should perform single traveral of the array.
• In case the multiple rearrangement exists, the solution can return any one of them.

Input : [1, 2, 3, 4, 5, 6, 7]

Output: [1, 3, 2, 5, 4, 7, 6] or [1, 5, 2, 6, 3, 7, 4], or any other valid combination..

Input : [6, 9, 2, 5, 1, 4]
Output: [6, 9, 2, 5, 1, 4] or [1, 5, 2, 6, 4, 9], or any other valid combination..

'''

from typing import List

def rearrange_in_place(nums: List[int]):
    '''
    Logic:
    - start from second element of the array and iterate through every other element
    - the number at each position should be greater than its neighbors, else swap the current number with max neighbor
    '''
    for i in range(1, len(nums), 2):
        # if prev index is valid and 
        # if the number at this index is less than prev number, replace it with prev number
        if i - 1 >= 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        
        # if next index is valid and
        # if the number (the number in this index might already be replaced by its prev number) at this index is less than next number, replace it with next number
        if i + 1 < len(nums) and nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
if __name__=="__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rearrange_in_place(nums=nums)
    print(nums)

