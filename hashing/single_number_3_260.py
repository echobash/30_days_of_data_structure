from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        result = []
        for num,freq in num_freq.items():
            if freq == 1:
                result.append(num)
        return result


sol = Solution()

nums = [1,2,1,3,2,5]
print(f"{nums = } {sol.singleNumber(nums) = }")

nums = [-1,0]
print(f"{nums = } {sol.singleNumber(nums) = }")

nums = [0,1]
print(f"{nums = } {sol.singleNumber(nums) = }")

nums = [0,1,4,4,2,3,2,3]
print(f"{nums = } {sol.singleNumber(nums) = }")
