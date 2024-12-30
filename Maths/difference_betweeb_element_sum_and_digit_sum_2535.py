from typing import List


class Solution:
    def sum_of_digits_of_a_num(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num = num // 10
        return digit_sum

    def differenceOfSum(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num

        digit_sum = 0
        for num in nums:
            digit_sum += self.sum_of_digits_of_a_num(num)

        return abs(sum - digit_sum)


sol = Solution()

nums = [1,15,6,3]
print(nums,sol.differenceOfSum(nums))

nums = [1,2,3,4]
print(nums,sol.differenceOfSum(nums))
