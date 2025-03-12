from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        positive_count = 0
        negative_count = 0
        for num in nums:
            if num < 0:
                negative_count += 1
            elif num > 0:
                positive_count += 1
        return max(positive_count,negative_count)


sol = Solution()


nums = [-2,-1,-1,1,2,3]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [-3,-2,-1,0,0,1,2]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [5,20,66,1314]
print(f"{nums = } {sol.maximumCount(nums) = }")
