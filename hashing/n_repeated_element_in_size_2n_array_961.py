from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_freq = Counter(nums)
        n = len(nums) // 2
        for num in nums:
            if num_freq[num] == n:
                return num


sol = Solution()

nums = [1,2,3,3]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")

nums = [2,1,2,5,3,2]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")

nums = [5,1,5,2,5,3,5,4]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")