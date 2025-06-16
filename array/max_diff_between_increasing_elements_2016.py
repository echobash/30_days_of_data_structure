from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_till_now = nums[0]
        max_diff = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= min_till_now:
                min_till_now = nums[i]
            else:
                max_diff = max(max_diff, nums[i] - min_till_now)
        return max_diff



sol = Solution()

nums = [7,1,5,4]
print(f" {nums = } | {sol.maximumDifference(nums) = }")

nums = [9,4,3,2]
print(f" {nums = } | {sol.maximumDifference(nums) = }")

nums = [1,5,2,10]
print(f" {nums = } | {sol.maximumDifference(nums) = }")

nums = [1,5]
print(f" {nums = } | {sol.maximumDifference(nums) = }")

nums = [5,2]
print(f" {nums = } | {sol.maximumDifference(nums) = }")
