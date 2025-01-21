from typing import List


class Solution:
    def findFirstOccurence(self, a, n, target):
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target:
                ans = mid
                right = mid - 1
            elif a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def findLastOccurence(self, a, n, target):
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target:
                ans = mid
                left = mid + 1
            elif a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        return [self.findFirstOccurence(nums, n, target), self.findLastOccurence(nums, n, target)]


sol = Solution()

nums = [5,7,7,8,8,10]
target = 8
print(nums,target,sol.searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(nums,target,sol.searchRange(nums, target))

nums = []
target = 7
print(nums,target,sol.searchRange(nums, target))

nums = [1,2,5,5,7,7,7,8,8,8,8,10]
target = 7
print(nums,target,sol.searchRange(nums, target))

nums = [1,2,5,5,7,7,7,8,8,8,8,10]
target = 8
print(nums,target,sol.searchRange(nums, target))
