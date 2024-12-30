from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            sum = 0
            for digit in str(nums[i]):
                sum += int(digit)
            nums[i] = sum

        return min(nums)


sol = Solution()

nums = [10,12,13,14]
print(nums,sol.minElement(nums))

nums = [1,2,3,4]
print(nums,sol.minElement(nums))

nums = [999,19,199]
print(nums,sol.minElement(nums))
