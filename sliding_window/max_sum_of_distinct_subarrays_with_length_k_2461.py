from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        freq_mapping = defaultdict(int)
        curr_sum = 0

        # 1st Window
        for i in range(k):
            curr_sum += nums[i]
            freq_mapping[nums[i]] += 1
        if len(freq_mapping) == k:
            max_sum = max(max_sum, curr_sum)

        # Remaining Windows
        for i in range(k, n):
            freq_mapping[nums[i - k]] -= 1
            if freq_mapping[nums[i - k]] == 0:
                del freq_mapping[nums[i - k]]

            freq_mapping[nums[i]] += 1
            curr_sum -= nums[i - k]
            curr_sum += nums[i]
            if len(freq_mapping) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum


sol = Solution()

arr = [1,5,4,2,9,9,9]
k = 3
print(f" {arr = } | {k = } | {sol.maximumSubarraySum(arr, k) = }")

arr = [4,4,4]
k = 3
print(f" {arr = } | {k = } | {sol.maximumSubarraySum(arr, k) = }")
