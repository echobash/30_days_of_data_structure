from collections import deque


class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        result = []

        negatives = deque()

        # First window
        for i in range(k):
            if arr[i] < 0:
                negatives.append(arr[i])
        m = len(negatives)
        result.append(negatives[0] if m else 0)

        # Rest windows
        for i in range(k, n):
            if arr[i] < 0:
                negatives.append(arr[i])

            if arr[i - k] >= 0:
                result.append(negatives[0] if len(negatives) else 0)
            else:
                negatives.popleft()
                result.append(negatives[0] if len(negatives) else 0)
        return result


sol = Solution()

nums = [-8, 2, 3, -6, 10]
k = 2
print(f" {nums = } | {k = } | {sol.firstNegInt(nums, k) = }")

nums = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(f" {nums = } | {k = } | {sol.firstNegInt(nums, k) = }")

nums = [12, 1, 3, 5]
k = 3
print(f" {nums = } | {k = } | {sol.firstNegInt(nums, k) = }")

nums = [1,-2,3,-4,5,-6,7,8]
k = 4
print(f" {nums = } | {k = } | {sol.firstNegInt(nums, k) = }")

nums = [1,-2,3,-4,1,1,1,3,5,-6,7,8,4,2]
k = 4
print(f" {nums = } | {k = } | {sol.firstNegInt(nums, k) = }")
