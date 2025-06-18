from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Our ans will lie b/w 1 to n because in the best case, all the elements of the array >= x
        n = len(nums)
        for i in range(1, n+1):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1
            if count == i:
                return i
        return -1


sol = Solution()

nums = [3,5]
print(f" {nums = } | {sol.specialArray(nums) = }")

nums = [0,0]
print(f" {nums = } | {sol.specialArray(nums) = }")

nums = [0,4,3,0,4]
print(f" {nums = } | {sol.specialArray(nums) = }")

nums = [0]
print(f" {nums = } | {sol.specialArray(nums) = }")

nums = [8]
print(f" {nums = } | {sol.specialArray(nums) = }")
