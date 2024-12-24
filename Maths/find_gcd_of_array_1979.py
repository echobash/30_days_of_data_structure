from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min = nums[0]
        max = nums[0]
        n = len(nums)
        gcd = 1

        for i in range(1, n):
            if nums[i] < min:
                min = nums[i]

            if nums[i] > max:
                max = nums[i]

        for i in range(1, max+1):
            if max % i == 0 and min % i == 0:
                gcd = i
        return gcd


sol = Solution()

nums = [2,5,6,9,10]
print(sol.findGCD(nums))

nums = [7,5,6,8,3]
print(sol.findGCD(nums))

nums = [3,3]
print(sol.findGCD(nums))
