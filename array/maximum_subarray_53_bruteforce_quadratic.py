from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum > max_sum:
                    max_sum = sum
        return max_sum


sol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f" {nums = } | {sol.maxSubArray(nums) = }")

nums = [1]
print(f" {nums = } | {sol.maxSubArray(nums) = }")

nums = [5,4,-1,7,8]
print(f" {nums = } | {sol.maxSubArray(nums) = }")
