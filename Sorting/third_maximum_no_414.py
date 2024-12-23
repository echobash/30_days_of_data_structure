from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        position = 1
        for i in range(len(nums)-1):
            if nums[i] !=nums[i+1]:
                position += 1
            if position == 3:
                return( nums[i+1])
        return nums[0]


solution = Solution()

nums = [3,2,1]
print(solution.thirdMax(nums))

nums = [1,2]
print(solution.thirdMax(nums))

nums = [2,2,3,1]
print(solution.thirdMax(nums))
