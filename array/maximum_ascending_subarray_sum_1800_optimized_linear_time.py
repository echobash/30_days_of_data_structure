from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                current_sum += nums[i+1]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i+1]
        return max(max_sum, current_sum)


sol = Solution()

nums = [10,20,30,5,10,50]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [10,20,30,40,50]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [50,40,30,20,10]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [12,17,15,13,10,11,12]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [12]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")
