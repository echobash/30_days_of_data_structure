from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        for i in range(n-1):
            if (nums[i] + nums[i+1]) % 2 == 0:
                return False
        return True


sol = Solution()

nums = [1]
print(f" {nums = } | {sol.isArraySpecial(nums) = }")

nums = [2,1,4]
print(f" {nums = } | {sol.isArraySpecial(nums) = }")

nums = [4,3,1,6]
print(f" {nums = } | {sol.isArraySpecial(nums) = }")