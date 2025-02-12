from typing import List


class Solution:
    def sum_of_digits(self,number):
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10
            number = number// 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        max_sum_of_pair = -1
        n = len(nums)
        for i in range(n-1):
            first_no_sum_of_digits = self.sum_of_digits(nums[i])
            for j in range(i+1, n):
                second_no_sum_of_digits = self.sum_of_digits(nums[j])
                if first_no_sum_of_digits == second_no_sum_of_digits:
                    max_sum_of_pair = max(max_sum_of_pair,nums[i] + nums[j])
        return max_sum_of_pair



sol = Solution()

nums = [18,43,36,13,7]
print(f"{nums = }  {sol.maximumSum(nums) = }")

nums = [10,12,19,14]
print(f"{nums = }  {sol.maximumSum(nums) = }")
