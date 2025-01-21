# Lower bound of a no means -
# 1. If the no exists, give first occurrence index
# 2. Else give the index where should have been inserted to maintain the sorted array
class Solution:
    def find_lower_bound(self, a, target):
        left,right = 0, len(a)-1
        ans=len(a)
        while left<=right:
            mid = (left+right)//2
            if a[mid] >= target:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans


sol = Solution()

nums = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3]
target = 2
print(nums, target,sol.find_lower_bound(nums, target))

nums=[3, 4, 4, 7, 8, 10]
target = 5
print(nums, target,sol.find_lower_bound(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 11
print(nums, target,sol.find_lower_bound(nums, target))

a = [0,0,1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
target = 1
print(a, target,sol.find_lower_bound(a, target))

target = -11
print(a, target,sol.find_lower_bound(a, target))


target = 11
print(a, target,sol.find_lower_bound(a, target))