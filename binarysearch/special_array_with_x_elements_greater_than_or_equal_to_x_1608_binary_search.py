from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Our ans will lie b/w 1 to n because in the best case, all the elements of the array >= x
        n = len(nums)
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num >= mid:
                    count += 1
            if count == mid:
                return mid
            elif count > mid:
                left = mid + 1
            else:
                right = mid - 1
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
