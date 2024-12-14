class Solution:
    def maxProductDifference(self, nums: [int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return (nums[n-1] * nums[n-2]) - (nums[0] * nums[1])


nums = [4,2,5,9,7,4,8]
sol = Solution()
print(nums, sol.maxProductDifference(nums))

nums = [5,6,2,7,4]
print(nums, sol.maxProductDifference(nums))