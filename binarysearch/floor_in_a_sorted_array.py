class Solution:
    def findFloor(self, a, target):
        left = 0
        right = len(a) - 1

        while left <= right:
            mid = (left + right) // 2

            if a[mid] == target:
                return mid
            elif a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right


sol = Solution()

nums = [1, 2, 8, 10, 11, 12, 19]
target = 0
print(nums, target,sol.findFloor(nums, target))

nums = [1, 2, 8, 10, 11, 12, 19]
target = 5
print(nums, target,sol.findFloor(nums, target))

nums = [3,4,4,4,4,4,4,4,6, 7, 9, 12, 16, 17]
target = 4
print(nums, target,sol.findFloor(nums, target))
