from typing import List


class Solution:
    def findFirstOccurence(self, position,nums,target):
        if position == 0:
            return 0
        while(nums[position] == target):
            if position == 0:
                return 0
            position -= 1
        return position + 1

    def findLastOccurence(self, position,nums,target):
        if position == len(nums)-1:
            return len(nums)-1
        while(nums[position] == target):
            if position == len(nums)-1:
                return len(nums)-1
            position += 1
        return position - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                first = self.findFirstOccurence(mid,nums,target)
                last = self.findLastOccurence(mid,nums,target)
                return [first, last]
            elif nums[mid] > target:
                # Move to left
                right = mid - 1
            else:
                # Move to right
                left = mid + 1
        return [-1,-1]



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
