from typing import List


class Solution:
    def longest_subarray_with_sum_less_than_equal_to_k(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_length = 0
        result = []

        for i in range(n):  # O(n)
            curr_sum = 0
            for j in range(i, n):  # O(n)
                curr_sum += nums[j]
                if curr_sum <= k:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        result = nums[i:j + 1]
        return result


sol = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(f" {nums = } | {k = } | {sol.longest_subarray_with_sum_less_than_k(nums, k) = }")

nums = [2,5,1,7,10]
k = 14
print(f" {nums = } | {k = } | {sol.longest_subarray_with_sum_less_than_k(nums, k) = }")
