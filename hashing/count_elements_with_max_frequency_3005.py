from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_freq = Counter(nums)
        count_of_elements = 0

        max_freq = max(num_freq.values())

        for element, freq in num_freq.items():
            if freq == max_freq:
                count_of_elements += freq
        return count_of_elements


sol = Solution()

nums = [1,2,2,3,1,4]
print(f" {nums = } | {sol.maxFrequencyElements(nums) = }")

nums = [1,2,3,4,5]
print(f" {nums = } | {sol.maxFrequencyElements(nums) = }")

nums = [1,2,3,4,3,5,3]
print(f" {nums = } | {sol.maxFrequencyElements(nums) = }")