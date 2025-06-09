from typing import List


class Solution:
    def longest_subarray_with_sum_equal_to_k(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_len = 0
        curr_sum = 0
        result = []
        left = 0  # update when shrinking

        for i in range(n):
            curr_sum += nums[i]

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == k:
                curr_len = i - left + 1
                if curr_len > max_len:
                    max_len = curr_len
                    result = nums[left:i + 1]
        return result


sol = Solution()

nums = [2,4,6,2,5,9,3,5,2,4]
k = 14
print(f" {nums = } | {k = } | {sol.longest_subarray_with_sum_equal_to_k(nums, k) = }")

nums = [2,4,6,2,1,3,5,2,3]
k = 14
print(f" {nums = } | {k = } | {sol.longest_subarray_with_sum_equal_to_k(nums, k) = }")

nums = [5,1,2,6,3]
k = 7
print(f" {nums = } | {k = } | {sol.longest_subarray_with_sum_equal_to_k(nums, k) = }")
