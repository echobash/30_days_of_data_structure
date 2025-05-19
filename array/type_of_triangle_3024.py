from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]
        if (a + b <= c) or (b + c <= a) or (c + a <= b):
            return "none"
        elif a == b == c:
            return "equilateral"
        elif a == b or b == c or c == a:
            return "isosceles"
        else:
            return "scalene"


sol = Solution()

nums = [3,3,3]
print(f" {nums = } | {sol.triangleType(nums) = }")

nums = [3,4,5]
print(f" {nums = } | {sol.triangleType(nums) = }")

nums = [13,4,5]
print(f" {nums = } | {sol.triangleType(nums) = }")