from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total_sum = 0
        count_of_nos = 0
        for num in nums:
            if num % 6 == 0:
                total_sum += num
                count_of_nos += 1
        if count_of_nos == 0:
            return total_sum
        return total_sum // count_of_nos


sol = Solution()

nums = [1,3,6,10,12,15]
print(f"{nums = } {sol.averageValue(nums) = }")

nums = [1,2,4,7,10]
print(f"{nums = } {sol.averageValue(nums) = }")
