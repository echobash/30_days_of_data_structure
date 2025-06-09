from typing import List


class Solution:
    def shortest_subarray_with_sum_less_than_equal_to_k(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        min_len = n
        curr_sum = 0
        left = 0
        result = []

        if n == 1:
            if nums[0] <= k:
                return [nums[0]]
            return []

        for i in range(n):
            curr_sum += nums[i]

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            curr_len = i - left + 1
            if curr_len and curr_len < min_len and curr_sum <= k:
                min_len = curr_len
                result = nums[left: i + 1]
        return result


sol = Solution()

nums = [2,5,1,10,10]
k = 14
print(f" {nums = } | {k = } | {sol.shortest_subarray_with_sum_less_than_equal_to_k(nums, k) = }")

nums = [2]
k = 3
print(f" {nums = } | {k = } | {sol.shortest_subarray_with_sum_less_than_equal_to_k(nums, k) = }")

nums = [2,4,6,2,5,9,3,5,2,4]
k = 23
print(f" {nums = } | {k = } | {sol.shortest_subarray_with_sum_less_than_equal_to_k(nums, k) = }")

nums = [12,4,6,5,9,3,5,2,4]
k = 4
print(f" {nums = } | {k = } | {sol.shortest_subarray_with_sum_less_than_equal_to_k(nums, k) = }")
