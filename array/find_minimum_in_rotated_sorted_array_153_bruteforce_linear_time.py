from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')
        for num in nums:
            if num < result:
                result = num
        return result


sol = Solution()

nums = [4,5,6,7,0,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [4,5,6,7,9,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [1]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [3,4,5,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [20,25,30,35,40,45]
print(f"{nums = } {sol.findMin(nums,) = }")



