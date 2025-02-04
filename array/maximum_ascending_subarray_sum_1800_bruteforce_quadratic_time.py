from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n-1):
            sum = nums[i]
            for j in range(i+1, n):
                if nums[j] > nums[j-1]:
                    sum += nums[j]
                else:
                    break
            max_sum = max(max_sum,sum)
        return max_sum



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
