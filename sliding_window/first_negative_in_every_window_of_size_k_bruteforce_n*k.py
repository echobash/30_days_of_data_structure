class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        result = []

        for i in range(n - k + 1):
            found_negative = False
            for j in range(i, i + k):
                if arr[j] < 0:
                    result.append(arr[j])
                    found_negative = True
                    break
            if not found_negative:
                result.append(0)
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
