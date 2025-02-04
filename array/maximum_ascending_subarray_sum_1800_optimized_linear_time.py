from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # Initialize max_sum(global) and current_sum(local) to first element. This handles array with single element too.
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(n-1):
            # Check for each element with next one is larger than current, then add the next element
            if nums[i] < nums[i+1]:
                current_sum += nums[i+1]
            else:
            # As soon as next one is found to be smaller, then we know, we should conclude this subarray here only and start new subarray. So update max_sum.
            # And also update current_sum to next number
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i+1]
        # It's possible that last element was larger too and was present in our ascending series, we should check the max again and return it.
        return max(max_sum, current_sum)




sol = Solution()

nums = [10,20,30,5,10,50]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [10,20,30,40,50]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [50,40,30,20,10]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [12,17,15,13,10,11,12]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")

nums = [12]
print(f" {nums = } | {sol.maxAscendingSum(nums) = }")
