from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_squares = 0
        for i in range(1,n+1):
            if n % i == 0:
                sum_of_squares += nums[i-1] ** 2
        return sum_of_squares


sol = Solution()

nums = [1,2,3,4]
print(f" {nums = } | {sol.sumOfSquares(nums) = }")

nums = [2,7,1,19,18,3]
print(f" {nums = } | {sol.sumOfSquares(nums) = }")