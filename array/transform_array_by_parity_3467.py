from typing import List

from collections import defaultdict


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums_frequency = defaultdict(int)
        result = []
        for num in nums:
            if num % 2 == 0:
                nums_frequency[0] += 1
            else:
                nums_frequency[1] += 1
        for _ in range(nums_frequency[0]):
            result.append(0)

        for _ in range(nums_frequency[1]):
            result.append(1)

        return result


sol = Solution()

nums = [4,3,2,1]
print(f"{nums= } {sol.transformArray(nums) = }")


nums = [1,5,1,4,2]
print(f"{nums= } {sol.transformArray(nums) = }")