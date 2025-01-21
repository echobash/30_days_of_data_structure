# Upper bound of a no means -
# Keep going into right till the current no > target and keep updating ans
# Once you reach a position where current no is no longer > target, we already have the greater no in ans
# Start with ans = len(n) so that if no greater than the last element is found, it is supposed be an len(a)

class Solution:
    def find_upper_bound(self, a, target):
        left,right = 0, len(a)-1
        ans=len(a)
        while left<=right:
            mid = (left+right)//2
            if a[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid+1
        return ans


sol = Solution()

a = [0,0,1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print(len(a))
target = 0
print(a, target,sol.find_upper_bound(a, target))

target = 1
print(a, target,sol.find_upper_bound(a, target))

target = 2
print(a, target,sol.find_upper_bound(a, target))

target = 2.5
print(a, target,sol.find_upper_bound(a, target))

target = 4
print(a, target,sol.find_upper_bound(a, target))

target = -11
print(a, target,sol.find_upper_bound(a, target))

target = 1123
print(a, target,sol.find_upper_bound(a, target))

a=[3,5,8,9,15,19]
target=9
print(a, target,sol.find_upper_bound(a, target))





