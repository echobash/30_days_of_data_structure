class Solution:
    def binary_search(self, left, right):

        target = 12
        if left > right:
            return -1
        while left <= right:
            mid = (right + left) // 2
            # print(left,right,mid)
            if a[mid] == target:
                return mid
            elif a[mid] > target:
                # Go to left
                right = mid - 1
            else:
                # Go to right
                left = mid + 1
            return self.binary_search(left, right)


a = [3, 4, 6, 7, 9, 12, 16, 17]
sol = Solution()
n = len(a)
left, right = 0, n - 1
print(sol.binary_search(left, right))