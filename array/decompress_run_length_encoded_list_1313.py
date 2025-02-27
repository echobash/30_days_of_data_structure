from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(0, n, 2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        return result



sol = Solution()

nums = [1,2,3,4]
print(f" {nums = } | {sol.decompressRLElist(nums) = }")

nums = [1,1,2,3]
print(f" {nums = } | {sol.decompressRLElist(nums) = }")

nums = [1,2,3,4,5,6,7,8]
print(f" {nums = } | {sol.decompressRLElist(nums) = }")

nums = [12,17,15,13,10,11]
print(f" {nums = } | {sol.decompressRLElist(nums) = }")
