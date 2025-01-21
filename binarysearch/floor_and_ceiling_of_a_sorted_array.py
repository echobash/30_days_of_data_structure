# Lower bound of a no means -
# 1. If the no exists, give first occurrence index
# 2. Else give the index where should have been inserted to maintain the sorted array
class Solution:
    def getFloor(self,a, n, target):
        if target < a[0]:
            return -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target:
                return a[mid]
            elif a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return a[right]

    def getCeiling(self,a, n, target):
        if target > a[n - 1]:
            return -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target:
                return a[mid]
            elif a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return a[left]

    def getFloorAndCeil(self,a, n, x):
        return self.getFloor(a, n, x), self.getCeiling(a, n, x)


sol = Solution()

nums = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3]
target = 2
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")

nums=[3, 4, 4, 7, 8, 10]
target = 5
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")


nums = [-1, 0, 3, 5, 9, 12]
target = 11
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")


a = [0,0,1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
target = 1
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")



target = -11
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")




target = 11
print(f"{nums= }, {target= }, sol= {sol.getFloorAndCeil(nums, len(nums), target)}")

