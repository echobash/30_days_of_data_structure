from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans


sol = Solution()

nums = [0,2,1,5,3,4]
print(nums, sol.buildArray(nums))

nums = [5,0,1,2,3,4]
print(nums, sol.buildArray(nums))