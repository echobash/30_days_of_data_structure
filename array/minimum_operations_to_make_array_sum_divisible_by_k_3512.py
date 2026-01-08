from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
"""
Logic behind this - 
[3,9,7]
3 + 9 + 7 = 19 
k = 5
we have to subract 1 mininum no of times from sum of the array so that it's divisible by k
so 19 % 5 = 4 i.e we have to subtract "1" four times so that it's divisible by k(5)

so sum(nums) % k
"""


sol = Solution()

nums = [3,9,7]
k = 5
print(f" {nums = } | {k = } | {sol.minOperations(nums, k) = }")

nums = [4,1,3]
k = 4
print(f" {nums = } | {k = } | {sol.minOperations(nums, k) = }")
