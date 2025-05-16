from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        result = []
        expected_count = len(nums) // 3
        for num, freq in nums_freq.items():
            if freq > expected_count:
                result.append(num)
        return result


sol = Solution()

nums = [3,2,3]
print(f"{ nums = } {sol.majorityElement(nums) =}")

nums = [1]
print(f"{ nums = } {sol.majorityElement(nums) =}")

nums = [1,2]
print(f"{ nums = } {sol.majorityElement(nums) =}")
