from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        for i in range(n - 2):
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1
        return count


sol = Solution()

nums = [1,2,1,4,1]
print(nums, sol.countSubarrays(nums))

nums = [1,1,1]
print(nums, sol.countSubarrays(nums))
