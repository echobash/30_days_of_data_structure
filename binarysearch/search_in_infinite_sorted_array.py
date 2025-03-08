class Solution:
    def searchInSorted(self, arr, k):
        n = len(arr)

        if n == 1:
            return arr[0] == k

        left, right = 0, 1

        while right < n and arr[right] < k:
            right *= 2

        # Once we come out from while loop, we know the desired right too
        # Implement binary search on left, right now
        right = min(right, n - 1)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return False


sol = Solution()
arr = [4, 5, 5, 7, 7, 8, 9]
k = 9
print(f"{arr = } {k = } {sol.searchInSorted(arr, k) = }")

arr = [3, 11, 19, 21, 42, 48, 204, 209, 294]
k = 209
print(f"{arr = } {k = } {sol.searchInSorted(arr, k) = }")

arr = [3, 11, 19, 21, 42, 48, 204, 209, 294]
k = 200
print(f"{arr = } {k = } {sol.searchInSorted(arr, k) = }")
