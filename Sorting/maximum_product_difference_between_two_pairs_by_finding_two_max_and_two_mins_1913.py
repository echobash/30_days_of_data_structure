import sys


class Solution:
    def maxProductDifference(self, nums: [int]) -> int:
        # Define explicit 32-bit bounds
        INT_MIN = -2147483648  # Minimum 32-bit integer
        INT_MAX = 2147483647  # Maximum 32-bit integer

        max1 = INT_MIN
        max2 = INT_MIN
        min1 = INT_MAX
        min2 = INT_MAX

        for num in nums:
            if num > max1:
                max1 = num

        for num in nums:
            if num > max2 and num != max1:
                max2 = num

        for num in nums:
            if num < min1:
                min1 = num

        for num in nums:
            if num < min2 and num != min1:
                min2 = num

        return (max1 * max2) - (min1 * min2)


nums = [4,2,5,9,7,4,8]
sol = Solution()
print(nums, sol.maxProductDifference(nums))

nums = [5,6,2,7,4]
print(nums, sol.maxProductDifference(nums))

nums = [1,6,7,5,2,4,10,6,4]
print(nums, sol.maxProductDifference(nums))