from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_of_one_digit_nums = 0
        for num in nums:
            if num // 10 == 0:
                sum_of_one_digit_nums += num
        return sum_of_one_digit_nums != int(sum(nums))/2


sol = Solution()

nums = [1,2,3,4,10]
print(nums,sol.canAliceWin(nums))

nums = [1,2,3,4,5,14]
print(nums,sol.canAliceWin(nums))

nums = [5,5,5,25]
print(nums,sol.canAliceWin(nums))
