from typing import  List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1
        return count


sol = Solution()

nums = [-1,1,2,3,1]
target = 2
print(nums, sol.countPairs(nums, target))

nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(nums, sol.countPairs(nums, target))

nums = [6,5,5,4,3,2,2,1,0]
target = 9
print(nums, sol.countPairs(nums, target))