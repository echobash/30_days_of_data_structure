from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(n):
            next_index = (i+1) % n
            max_diff = max(max_diff, abs(nums[i] - nums[next_index]))
        return max_diff


sol = Solution()

nums = [1,2,4]
print(f" {nums = } | {sol.maxAdjacentDistance(nums) = }")

nums = [-5,-10,-5]
print(f" {nums = } | {sol.maxAdjacentDistance(nums) = }")