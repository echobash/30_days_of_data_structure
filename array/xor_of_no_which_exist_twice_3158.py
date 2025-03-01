from typing import List
from collections import Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        num_count_mapping = Counter(nums)

        xor_result = 0
        for num,frequency in num_count_mapping.items():
            if frequency == 2:
                xor_result ^= num
        return xor_result


sol = Solution()

nums = [1,2,1,3]
print(f" {nums = } | {sol.duplicateNumbersXOR(nums) = }")

nums = [1,2,3]
print(f" {nums = } | {sol.duplicateNumbersXOR(nums) = }")

nums = [1,2,2,1]
print(f" {nums = } | {sol.duplicateNumbersXOR(nums) = }")