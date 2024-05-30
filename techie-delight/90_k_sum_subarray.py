'''

Given an integer array, find all contiguous subarrays with a given sum `k`.

Input : nums[] = [3, 4, -7, 1, 3, 3, 1, -4], k = 7
Output: {(3, 4), (3, 4, -7, 1, 3, 3), (1, 3, 3), (3, 3, 1)}

Since the input can have multiple subarrays with sum `k`, the solution should return a set containing all the distinct subarrays.

'''

from typing import List, Set, Tuple


def get_all_sub_arrays(nums: List[int], k: int) -> Set[Tuple[int]]:
    result = set()
    prefix_sum = 0
    sum_dict = {0: [-1]}  # Initialize with 0: [-1] to handle the case when the subarray starts from index 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        complement = prefix_sum - k
        if complement in sum_dict:
            for j in sum_dict[complement]:
                start_index = j + 1
                result.add(tuple(nums[start_index:i + 1]))

        if prefix_sum not in sum_dict:
            sum_dict[prefix_sum] = []

        sum_dict[prefix_sum].append(i)

    return result

if __name__=="__main__":
    nums = [1, -1, 1, -1, 1]
    k = 0
    ans = get_all_sub_arrays(nums=nums, k=k)
    print(ans)