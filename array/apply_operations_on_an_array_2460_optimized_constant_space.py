from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Simulate the given condition
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        # Shift all the zeroes to right
        zero_index = -1
        for i in range(n):
            if nums[i] == 0 and zero_index == -1:
                zero_index = i
            elif nums[i] != 0 and zero_index != -1:
                (nums[i], nums[zero_index]) = (nums[zero_index], nums[i])
                zero_index = zero_index + 1
        return nums


sol = Solution()

nums = [1,2,2,1,1,0]
print(f" {nums = } | {sol.applyOperations(nums) = }")

nums = [0,1]
print(f" {nums = } | {sol.applyOperations(nums) = }")

nums =  [1,0,2,2,1,1,0]
print(f" {nums = } | {sol.applyOperations(nums) = }")