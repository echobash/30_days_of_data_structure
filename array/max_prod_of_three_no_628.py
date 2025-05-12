from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums, reverse = True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-2] * nums[-1])


sol = Solution()

nums = [1,2,3]
print(f"{nums = } {sol.maximumProduct(nums) = } ")

nums = [1,2,3,4]
print(f"{nums = } {sol.maximumProduct(nums) = } ")

nums = [-1,-2,-3]
print(f"{nums = } {sol.maximumProduct(nums) = } ")
