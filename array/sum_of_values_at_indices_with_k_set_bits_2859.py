from typing import List


class Solution:
    def has_k_set_bits(self, i, k):
        return bin(i).count('1') == k

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        for i, num in enumerate(nums):
            if self.has_k_set_bits(i, k):
                total_sum += num
        return total_sum


sol = Solution()

nums = [5,10,1,5,2]
k = 1
print(f" {nums = } | {sol.sumIndicesWithKSetBits(nums, k) = }")

nums = [4,3,2,1]
k = 2
print(f" {nums = } | {sol.sumIndicesWithKSetBits(nums, k) = }")
