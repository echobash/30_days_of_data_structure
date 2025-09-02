from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0,1
        hills_or_valley_count = 0

        while j != n-1:
            if nums[i] < nums[j] and nums[j] > nums[j+1]:
                hills_or_valley_count += 1
                i = j
            elif  nums[i] > nums[j] and nums[j] < nums[j+1]:
                hills_or_valley_count += 1
                i = j
            j += 1
        return hills_or_valley_count


sol = Solution()

nums = [2,4,1,1,6,5]
print(f" {nums = }|   {sol.countHillValley(nums) = }")

nums = [6,6,5,5,4,1]
print(f" {nums = }|   {sol.countHillValley(nums) = }")