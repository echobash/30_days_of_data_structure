class Solution:
    def peakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        if nums[1] < nums[0]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i


sol = Solution()

nums = [1, 2, 4, 5, 7, 8, 3]
print(f"{nums= } {sol.peakElement(nums)= }")

nums = [10, 20, 15, 2, 23, 90, 80]
print(f"{nums= } {sol.peakElement(nums)= }")

nums = [1, 2, 3]
print(f"{nums= } {sol.peakElement(nums)= }")

nums = [1,2,1,3,5,6,4]
print(f"{nums= } {sol.peakElement(nums)= }")

nums = [1,2,3,1]
print(f"{nums= } {sol.peakElement(nums)= }")
