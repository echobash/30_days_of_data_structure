from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            total_sum += (-1) ** i * nums[i]

        return total_sum
"""
Logic behind this - 
1,3,5,7
1 -3 + 5 -7
(-1 ** i ) * nums[i]

We have to add even index element and subtract odd index element
so we'll multiply the element with (-1) ** i where i is index
so (-1) ** 1 = -1
(-1) ** 2 = 1
(-1) ** 3 = -1
"""


sol = Solution()

nums = [1,3,5,7]
print(f" {nums = } | {sol.alternatingSum(nums) = }")

nums = [100]
print(f" {nums = } | {sol.alternatingSum(nums) = }")
