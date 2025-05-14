from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
                max_ones = max(max_ones,count)
            else:
                count = 0
        return max_ones


sol = Solution()

arr = [1,1,0,1,1,1]
print(f" {arr = } | {sol.findMaxConsecutiveOnes(arr) = }")

arr = [1,0,1,1,0,1]
print(f" {arr = } | {sol.findMaxConsecutiveOnes(arr) = }")

arr = [0]
print(f" {arr = } | {sol.findMaxConsecutiveOnes(arr) = }")

arr = [1]
print(f" {arr = } | {sol.findMaxConsecutiveOnes(arr) = }")