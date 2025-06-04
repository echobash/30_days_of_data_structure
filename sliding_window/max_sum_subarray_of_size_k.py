class Solution:
    def maximumSumSubarray(self, arr, k):
        n = len(arr)
        if k > n:
            raise ValueError(f" {nums = } | {k = } | Given Subarray size greater than actual array size")

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum


sol = Solution()

nums = [100, 200, 300, 400]
k = 2
print(f" {nums = } | {k = } | {sol.maximumSumSubarray(nums, k) = }")

nums = [100, 200, 300, 400]
k = 4
print(f" {nums = } | {k = } | {sol.maximumSumSubarray(nums, k) = }")

nums = [100, 200, 300, 400]
k = 1
print(f" {nums = } | {k = } | {sol.maximumSumSubarray(nums, k) = }")

#
nums = [100, 200, 300, 400]
k = 5
try:
    print(f" {nums = } | {k = } | {sol.maximumSumSubarray(nums, k) = }")
except ValueError as e:
    print(e)

nums = [100, 200, 300, 400]
k = 3
print(f" {nums = } | {k = } | {sol.maximumSumSubarray(nums, k) = }")