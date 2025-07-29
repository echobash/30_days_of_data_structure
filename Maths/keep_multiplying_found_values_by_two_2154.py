from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)

        if original not in nums_set:
            return original

        while original in nums_set:
            original *= 2

        return original


sol = Solution()

nums = [5,3,6,1,12]
original = 3
print(f"{nums = } {original = } {sol.findFinalValue(nums, original) = }")

nums = [2,7,9]
original = 4
print(f"{nums = } {original = } {sol.findFinalValue(nums, original) = }")