from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_no = min(nums)
        max_no = max(nums)

        for num in nums:
            if num != min_no and num != max_no:
                return num

        return -1


sol = Solution()

nums = [3,2,1,4]
print(f"{nums = } {sol.findNonMinOrMax(nums) = }")

nums = [1,2]
print(f"{nums = } {sol.findNonMinOrMax(nums) = }")

nums = [2,1,3]
print(f"{nums = } {sol.findNonMinOrMax(nums) = }")
