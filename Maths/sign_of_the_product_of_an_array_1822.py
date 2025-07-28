from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            else:
                ans = -1 * ans if num < 0 else ans
        return ans

sol = Solution()

nums = [-1,-2,-3,-4,3,2,1]
print(f"{nums = } {sol.arraySign(nums) = } ")

n = [-1,1,1,17,-1]
print(f"{nums = } {sol.arraySign(nums) = } ")

n = [-1,1,-1,1,5]
print(f"{nums = } {sol.arraySign(nums) = } ")

n = [-1,1,-1,1,-1]
print(f"{nums = } {sol.arraySign(nums) = } ")

nums = [1,5,0,2,-3]
print(f"{nums = } {sol.arraySign(nums) = }")
