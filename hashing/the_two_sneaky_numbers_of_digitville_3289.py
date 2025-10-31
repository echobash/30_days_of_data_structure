from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        result = []
        for num, freq in num_freq.items():
            if freq == 2:
                result.append(num)
        return result


sol = Solution()

nums = [0,1,1,0]
print(f"{nums = } | {sol.getSneakyNumbers(nums) = }")

nums = [0,3,2,1,3,2]
print(f"{nums = } | {sol.getSneakyNumbers(nums) = }")

nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(f"{nums = } | {sol.getSneakyNumbers(nums) = }")