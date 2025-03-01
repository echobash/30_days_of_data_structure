from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        # Simulate the given condition
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        # Shift all the zeroes to right
        # [1,0,2,0,0,1]
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1

        for j in range(n):
            if nums[j] != 0:
                result.append(nums[j])

        for k in range(zero_count):
            result.append(0)

        return result


sol = Solution()

nums = [1,2,2,1,1,0]
print(f" {nums = } | {sol.applyOperations(nums) = }")

nums = [0,1]
print(f" {nums = } | {sol.applyOperations(nums) = }")

nums =  [1,0,2,2,1,1,0]
print(f" {nums = } | {sol.applyOperations(nums) = }")