from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        result[0] = nums[0]
        for i in range(1,n):
            result[i] = nums[i] + result[i-1]
        return result



sol = Solution()

nums = [1,2,3,4]
print(nums, sol.runningSum(nums))

nums = [1,1,1,1,1]
print(nums, sol.runningSum(nums))

nums = [3,1,2,10,1]
print(nums, sol.runningSum(nums))
